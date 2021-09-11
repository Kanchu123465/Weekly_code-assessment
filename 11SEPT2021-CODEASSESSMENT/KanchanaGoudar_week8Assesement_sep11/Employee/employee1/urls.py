from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('views/',views.Viewallemployee,name='Viewallemployee'),
    path('update/',views.Updateemployee,name='Updateemployee'),
    path('login/',views.login,name='login'),
    path('logincheck/',views.login_check,name='login_check'),
    

    path('employeeaddapi/',views.employeeadd,name='employeeadd'),
    path('viewallapi/',views.employeeviewall,name='employeeviewall'),
    path('viewapi/<fetchid>',views.employeeview,name='employeeview'),
    path('update_searchapi/',views.update_searchapi,name='update_searchapi'),
    path('update_data/',views.update_data_read,name='update_data_read'),
    path('logout/',views.logout_user,name='logout_user'),
]
