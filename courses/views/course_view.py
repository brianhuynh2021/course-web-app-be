from rest_framework.views import APIView
from rest_framework.response import Response
from courses.serializers.course_serializer import CourseSerializer
from courses.cruds.course_crud import get_all_courses, get_course_by_id
from rest_framework import status


class CourseListView(APIView):
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
    def get(self, request, course_id):
        course = get_course_by_id(course_id)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
