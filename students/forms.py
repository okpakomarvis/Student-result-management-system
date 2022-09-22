from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['student_reg']
        widgets = {
            'student_name'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_matric_no'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'student_email'  :   forms.EmailInput(attrs={'class':'form-control'}),
            'student_gender'  :   forms.Select(attrs={'class':'form-control'}),
            'student_programme'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_level'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'student_course'  :   forms.Select(attrs={'class':'form-control'}),
            'student_date_of_birth'  :   forms.DateInput(attrs={'class':'form-control'}),
        }