from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.Addfaculty,name='Addfaculty'),
    path('login',views.facultylogin,name='facultylogin'),
    path('add/',views.Facultyadd,name='Facultyadd'),
    path('viewall/',views.Viewallfaculty,name='Viewallfaculty'),
    path('view/<fetchid>',views.Faculty_details,name='Faculty_details'),
    path('fcode/<fcode>',views.FacultySearch,name='FacultySearch'),
]
