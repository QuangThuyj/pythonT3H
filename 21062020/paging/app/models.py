from django.db import models


# Create your models here.


class Student(models.Model):
    studentNo = models.CharField(max_length=30, unique=True)
    studentName = models.CharField(max_length=100)

    def __str__(self):
        return self.studentName
