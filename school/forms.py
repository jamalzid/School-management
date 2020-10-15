from django import forms
from .models import AdminHod,Staff,Student,Course

class AddAdminForm(forms.ModelForm):
    class Meta:
        model = AdminHod
        fields='__all__'


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff

        fields = '__all__'



class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = '__all__'
class AddCourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
