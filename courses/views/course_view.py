from rest_framework.views import APIView
from rest_framework.response import Response
from courses.serializers.course_serializer import CourseSerializer
from courses.cruds.course_crud import get_all_courses, get_course_by_id
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import time
from rest_framework.permissions import IsAuthenticated

@method_decorator(cache_page(60*5), name='dispatch')
class CourseListView(APIView):
    def get(self, request):
        try:
            start_time = time.time()
            courses = get_all_courses()
            serializer = CourseSerializer(courses, many=True)
            end_time = time.time()
            print(f"Duration {end_time - start_time:.4f}")
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": "Failed to get courses", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class CourseDetailView(APIView):
    def get(self, request, course_id):
        course = get_course_by_id(course_id)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

class CourseCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
