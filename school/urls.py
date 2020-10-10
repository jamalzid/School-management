from .views import *
from django.urls import path
app_name='school'
urlpatterns = [
    path('dash/',index,name='admin'),
    path('add_admin/', add_admin, name='add_admin'),
    path('add_staff/', add_staff, name='add_staff'),
    path('add_student/', add_student, name='add_student'),


]
