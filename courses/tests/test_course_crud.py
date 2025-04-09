import uuid
from django.test import TestCase
from courses.models import Course
from courses.cruds.course_crud import get_all_courses, get_course_by_id


class GetAllCoursesTest(TestCase):
    def setUp(self):
        Course.objects.create(
            id=uuid.uuid4(),
            title="Course 1",
            length=120,
            description="Test 1",
            cost=120,
            thumbnail="https://example.com/img1.jpg"
        )
        
        Course.objects.create(
            id=uuid.uuid4(),
            title="Course 2",
            length=240,
            description="Test 2",
            cost=20,
            thumbnail="https://example.com/img2.jpg"
        )
        
    def test_get_all_courses_returns_all_courses(self):
        courses = get_all_courses()
        self.assertEqual(len(courses), 2)
        
class GetCourseByIdTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            id=uuid.uuid4(),
            title="Special Course",
            length=150,
            description="Unique course",
            cost=99,
            thumbnail="https://example.com/special.jpg"
        )

    def test_get_course_by_id_returns_correct_course(self):
        found = get_course_by_id(self.course.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Special Course")

    def test_get_course_by_id_returns_none_for_invalid_id(self):
        fake_id = uuid.uuid4()
        found = get_course_by_id(fake_id)
        self.assertIsNone(found)