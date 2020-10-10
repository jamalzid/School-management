from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AdminHod)
class AdminAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(LeaveReortStudent)
class LeaveReortStudentAdmin(admin.ModelAdmin):
    pass


@admin.register(LeaveReortStaff)
class LeaveReortStaffAdmin(admin.ModelAdmin):
    pass



@admin.register(NotificationStudent)
class NotificationStudentAdmin(admin.ModelAdmin):
    pass


@admin.register(NotificationStaff)
class NotificationStaffAdmin(admin.ModelAdmin):
    pass


