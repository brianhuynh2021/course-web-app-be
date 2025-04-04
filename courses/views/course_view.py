from rest_framework.views import APIView
from rest_framework.response import Response
from courses.serializers.course_serializer import CourseSerializer
from courses.cruds.course_crud import get_all_courses


class CourseListView(APIView):
    def get(self, request):
        courses = get_all_courses()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)