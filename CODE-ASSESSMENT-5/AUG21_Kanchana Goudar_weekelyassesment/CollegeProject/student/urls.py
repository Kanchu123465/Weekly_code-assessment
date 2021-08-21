from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Addstudent,name='Addstudent'),
    path('add/',views.Studentadd,name='Studentadd'),
    path('viewall/',views.Viewallstudent,name='Viewallstudent'),
    path('view/<fetchid>',views.Student_details,name='Student_details'),
    path('admno/<admno>',views.StudentSearch,name='StudentSearch'),
]