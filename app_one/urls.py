from django.urls import path
from app_one import views

app_name = 'app_one'

urlpatterns = [
    path('list_school/',views.School_List.as_view(),name='list_one'),
    path('list_student/',views.Student_List.as_view(),name='list_two')



]

