from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


# Create your models here.
Gender_Choices=(
    ('Male', 'Male'),
    ('Female', 'Female'),

)

class UserType(User):
    user_type_data = (1, 'Admin'), (2, 'Staff'), (3, 'Student')
    user_type=models.CharField(max_length=7,choices=user_type_data)
class AdminHod(models.Model):
    # admin=models.OneToOneField(UserType,related_name='Admin',on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    created_at=models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects=models.Manager()
    def __str__(self):
        return str(self.user)

class Staff(models.Model):
    # staff = models.OneToOneField(UserType,related_name='Staff', on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    gender = models.CharField(choices=(Gender_Choices), max_length=6)

    adress = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    subjects = models.Manager()

    def __str__(self):
        return str(self.user)


class Course(models.Model):
    name=models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()


    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()


    def __str__(self):
        return self.name
class Student(models.Model):
    # student = models.OneToOneField(UserType,related_name='Student', on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
   
    gender = models.CharField(choices=Gender_Choices,max_length=6)
    image = models.ImageField(
    upload_to='media/profiles_pic/', default='static/img/student_icon.jpg',null=True,blank=True)
    adress=models.TextField()
    session_start=models.DateField()
    session_end = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)

class Attendance(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.subject

class AttendanceReport(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.student
class LeaveReortStudent(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    leave_date=models.DateTimeField(auto_now_add=True)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()
    def __str__(self):
            return self.student


class LeaveReortStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_date = models.DateTimeField(auto_now_add=True)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.staff


class LeaveReortStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=250)
    feedback_reply = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.student


class LeaveReortStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=250)
    feedback_reply = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.staff


class NotificationStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.student


class NotificationStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    subjects = models.Manager()

    def __str__(self):
        return self.staff

@receiver(post_save, sender=UserType)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHod.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(staff=instance)
        if instance.user_type == 3:
            Student.objects.create(student=instance)
@receiver(post_save, sender=UserType)
def _post_save_receiver(sender,instance, **kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.student.save()


