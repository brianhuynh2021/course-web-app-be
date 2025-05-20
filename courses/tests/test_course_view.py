from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from unittest.mock import patch
from courses.models.course_model import Course
from courses.serializers.course_serializer import CourseSerializer
from django.contrib.auth.models import User
import uuid


class CourseDetailViewMockTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345678')
        self.client.force_authenticate(user=self.user)
        
    @patch("courses.views.course_view.get_course_by_id")
    def test_course_detail_success(self, mock_get_course):
        # fake course
        course = Course(
            id=uuid.uuid4(),
            title="Mocked Course",
            length=90,
            description="Test Desc",
            cost=50,
            thumbnail="http://test.com/img.jpg",
        )
        mock_get_course.return_value = course

        url = reverse("course-detail", args=[course.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Mocked Course")

    @patch("courses.views.course_view.get_course_by_id")
    def test_course_detail_not_found(self, mock_get_course):
        mock_get_course.return_value = None

        url = reverse("course-detail", args=[uuid.uuid4()])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.data)