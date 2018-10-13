from django.shortcuts import render
from app_one import models
from django.views.generic import ListView,TemplateView
# Create your views here.
class Index(TemplateView):
    template_name = 'app_one/index.html'

class School_List(ListView):
    model = models.School
    template_name = 'app_one/school_models.html'


class Student_List(ListView):
    model = models.Student
    template_name = 'app_one/student_models.html'
