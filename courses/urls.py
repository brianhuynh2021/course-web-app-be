from django.urls import path
from .views import CourseListView, CourseDetailView, AgentCourseView


urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<uuid:course_id>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/agent/respond/', AgentCourseView.as_view(), name='agent-response')
]
