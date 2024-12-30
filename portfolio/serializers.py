from rest_framework import serializers
from .models import Student, Project, Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'university', 'faculty', 'course_number')

class ProjectSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'field', 'description', 'students')

class EventSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'field', 'description', 'address', 'students')
