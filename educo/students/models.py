from django.db import models
from courses.models import Course

class Student(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50, verbose_name="First Name (French)")
    last_name = models.CharField(max_length=50, verbose_name="Last Name (French)")
    first_name_in_arabic = models.CharField(max_length=100, blank=True, null=True, verbose_name="First Name (Arabic)")
    last_name_in_arabic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Last Name (Arabic)")
    id_card_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    
    # Parent/Guardian Information
    parent_name = models.CharField(max_length=100)
    relationship_choices = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian'),
    ]
    relationship = models.CharField(max_length=10, choices=relationship_choices)
    parent_email = models.EmailField(blank=True, null=True)
    parent_phone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Dropped', 'Dropped'),
    ], default='Not Started')
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total course fee")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Amount already paid")
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.title}"

class PaymentTransaction(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, choices=[
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
    ], default='Cash')
    
    def __str__(self):
        return f"{self.enrollment.student.first_name} {self.enrollment.student.last_name} - {self.amount} MAD on {self.date}"
