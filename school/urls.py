
from .views import *
from django.views.generic import TemplateView
from django.urls import path
app_name='school'
urlpatterns =[
    path('', index, name='index'),

    path('dash/',dash,name='dash'),
    path('add_admin/', add_admin, name='add_admin'),
    path('add_staff/', add_staff, name='add_staff'),
    path('add_student/', add_student, name='add_student'),
    path('add_course/', add_course, name='add_course'),
    path('all_admins/', AdminList.as_view(), name='all_admins'),
    path('all_staffs/', StaffList.as_view(), name='all_staffs'),
    path('all_students/', StudentList.as_view(), name='all_students'),
    




]
