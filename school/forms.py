from django import forms
from .models import AdminHod,Staff,Student

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
