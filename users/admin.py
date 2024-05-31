from django.contrib import admin

from materials.models import Course, Lesson
from users.models import Payments, User

# Register your models here.
admin.site.register(Payments)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
