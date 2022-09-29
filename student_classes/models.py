from django.db import models
from django.urls import reverse
# Create your models here.

class StudentClass(models.Model):
    class_name              =   models.CharField(max_length=200, help_text='Eg- Computer science, Education etc')
    class_code              =   models.CharField(max_length=100, help_text='Eg- csc etc') 
    section                 =   models.CharField(max_length=100, help_text='Eg- first-semester, second-semester etc')
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('student_classes:class_list')

    def __str__(self):
       return "%s Section-%s"%(self.class_name, self.section)
