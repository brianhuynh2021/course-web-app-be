from rest_framework.views import APIView
from rest_framework.response import Response
from courses.serializers.course_serializer import CourseSerializer
from courses.cruds.course_crud import get_all_courses, get_course_by_id
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db import connection

class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        result = {"server": "up", "status": "ok"}
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
                result["db"] = "connected"
        except Exception as e:
            result['db'] = "error"
            result['status'] = "fail"
            result['detail'] = str(e)
        return Response(result, status=200 if result["status"] == "ok" else 500)
class CourseListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            courses = get_all_courses()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": "Failed to get courses", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class CourseDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, course_id):
        course = get_course_by_id(course_id)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

class CourseCreateView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
