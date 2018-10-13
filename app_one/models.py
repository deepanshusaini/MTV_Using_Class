from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50,primary_key=True)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.school_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student_name