from django.db import models
from django.shortcuts import reverse

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True)
    major_title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.major_id)

class Student(models.Model):
    studentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    major_id = models.ForeignKey( Major , on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True ,  blank=True)
    address = models.CharField(max_length=50, null=True,  blank=True)
    hobby = models.CharField(max_length=50, null=True,  blank=True)
    skill = models.CharField(max_length=50, null=True,  blank=True)

    def __str__(self):
        return self.name 

    #기능 성공 시 돌아갈 url
    def get_absolute_url(self):
        return reverse('crud:list')