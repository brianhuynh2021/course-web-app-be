from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        
    def create(self, validated_data):
        return super().create(validated_data)