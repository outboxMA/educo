from django.db import models
from django.contrib.auth.models import User
from instructors.models import Instructor 

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='courses')
    duration = models.PositiveIntegerField(help_text="Duration of the course in hours")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the course")
    cover_image = models.ImageField(upload_to='course_covers/', blank=True, null=True, help_text="Upload a cover image for the course")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sessions')
    session_title = models.CharField(max_length=255)
    session_date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)  # For physical location
    is_online = models.BooleanField(default=False)  # Whether the session is online or in-person
    session_link = models.URLField(blank=True, null=True)  # If online, link to session (e.g., Zoom)

    def __str__(self):
        return f"{self.course.title} - {self.session_title} ({self.session_date})"
