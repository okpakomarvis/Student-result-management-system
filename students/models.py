from django.db import models
from student_classes.models import StudentClass
from django.urls import reverse
from datetime import date
# Create your models here.

class Student(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    student_name = models.CharField(max_length=100)
    student_matric_no = models.CharField(max_length=200,unique=True)
    student_email = models.EmailField()
    student_gender = models.CharField(max_length=8, choices=select_gender)
    student_programme=models.CharField(max_length=200)
    student_level=models.IntegerField()
    student_course = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_date_of_birth = models.DateField()
    student_reg = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.student_name