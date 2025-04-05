from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'bio', 'profile_picture', 'email']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Short biography of the instructor.'}),
        }
