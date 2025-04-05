from django import forms
from .models import Course, Session, Instructor
from instructors.models import Instructor

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'duration', 'start_date', 'end_date', 'is_active', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a description of the course here.'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_title', 'session_date', 'location', 'is_online', 'session_link']
        widgets = {
            'session_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }