from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import Subscription, User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(
            name="TestCourse", description="TestDescription", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="TestLesson",
            description="TestDescription",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lessons_create")
        data = {
            "name": "Test Lesson1",
            "description": "Test Lesson1 Description",
            "video_url": "https://www.youtube.com/watch?v=g-I5-m5jYvE",
            "course": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Test Lesson change",
            "video_url": "https://www.youtube.com/watch?v=g-I5-m5jYvE",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Test Lesson change")

    def test_lesson_destroy(self):
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_url": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(
            name="Подписка", description="Тест подписки", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = reverse("users:subscriptions_create")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data, {"message": f"подписка на курс {self.course.name} добавлена"}
        )

    def test_unsubscribe(self):
        url = reverse("users:subscriptions_create")
        data = {"course": self.course.pk}
        Subscription.objects.create(course=self.course, user=self.user)
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data, {"message": f"подписка на курс {self.course.name} удалена"}
        )
