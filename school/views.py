from django.utils.translation import gettext as _

from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request,*args,**kwargs):
    admins = AdminHod.subjects.all()
    staffs = Staff.subjects.all()
    students = Student.objects.all()
    online = User.objects.filter(is_staff=True)

    context={
        'admins':admins,
        'staffs': staffs,
        'students': students,

    }

    return render(request,'school/index.html',context)


def add_admin(request, *args, **kwargs):
    if request.method=='POST':
        try:
            form = AddAdminForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Admins"))
                return redirect('school:admin')
        except :
            messages.error(request, _('Failed'))
    else:
        form = AddAdminForm()
    context = {
        'form':form,
    }

    return render(request, 'school/add_admin.html', context)

             
def add_staff(request, *args, **kwargs):
    if request.method=='POST':
        try:
            form = AddStaffForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Staffs"))
        except :
            messages.error(request, _('Failed'))
        
        return redirect('school:admin')
        
    else:
        form = AddStaffForm()
    context = {
        'form':form,
    }

    return render(request, 'school/add_staff.html', context)


def add_student(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            form = AddStudentForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, _("User Added To Students"))
        except:
            messages.error(request, _('Failed'))
        
        return redirect('school:admin')
    else:
        form = AddStudentForm()
    context = {
        'form': form,
    }

    return render(request, 'school/add_student.html', context)
