from django.utils.translation import gettext as _

from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
def index(request,*args,**kwargs):
    context={
        
    }

    return render(request,'school/index.html',context)
class AdminList(ListView):
    queryset = AdminHod.subjects.all()
    template_name='school/template_list/admin_list.html'


class StaffList(ListView):
    queryset = Staff.subjects.all()
    template_name = 'school/template_list/staff_list.html'


class StudentList(ListView):
    queryset = Student.objects.all()
    
    template_name = 'school/template_list/student_list.html'


@user_passes_test(lambda u: u.is_superuser)
def dash(request,*args,**kwargs):
    admins = AdminHod.subjects.all()
    staffs = Staff.subjects.all()
    students = Student.objects.all()
    online = User.objects.filter(is_staff=True)

    context={
        'admins':admins,
        'staffs': staffs,
        'students': students,

    }

    return render(request,'school/dash.html',context)


@user_passes_test(lambda u: u.is_superuser)
def add_admin(request, *args, **kwargs):
    if request.method=='POST':
        try:
            form = AddAdminForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Admins"))
                return redirect('school:dash')
        except :
            messages.error(request, _('Failed'))
    else:
        form = AddAdminForm()
    context = {
        'form':form,
    }
    return render(request, 'school/add_admin.html', context)

@user_passes_test(lambda u: u.is_superuser)             
def add_staff(request, *args, **kwargs):
    if request.method=='POST':
        try:
            form = AddStudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Staffs"))
        except :
            messages.error(request, _('Failed'))
        
        return redirect('school:dash')
        
    else:
        form = AddStaffForm()
    context = {
        'form':form,
    }
    return render(request, 'school/add_staff.html', context)

@user_passes_test(lambda u: u.is_superuser)
def add_student(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            form = AddStudentForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Students"))
        except:
            messages.error(request, _('Failed'))
        return redirect('school:dash')
    
    form = AddStudentForm()
    context = {
        'form': form,
    }
    return render(request, 'school/add_student.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_course(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            form = AddCourseForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, _("Course Added Successefuly"))
        except:
            messages.error(request, _('Failed'))

        return redirect('school:dash')
    else:
        form = AddCourseForm()
    context = {
        'form': form,
    }

    return render(request, 'school/add_Course.html', context)
