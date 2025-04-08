from courses.models import Course


def get_all_courses():
    return Course.objects.all()

def get_course_by_id(course_id):
    return Course.objects.filter(id=course_id).first()
