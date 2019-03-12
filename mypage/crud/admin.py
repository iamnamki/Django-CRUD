from django.contrib import admin
from .models import Student
from .models import Major

admin.site.register(Student) #어드민에서 확인
admin.site.register(Major) #어드민에서 확인