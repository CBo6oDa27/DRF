from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="video_url")]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    course_lessons = LessonSerializer(source="lesson_set", many=True)

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course.id).count()

    class Meta:
        model = Course
        fields = ("name", "description", "course_lessons", "lessons_count")
