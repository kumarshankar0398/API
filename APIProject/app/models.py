from django.db import models

# Create your models here.
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=150)
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])

    def __str__(self):
        return f"Name: {self.name}"
