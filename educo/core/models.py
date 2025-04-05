from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    type = models.CharField(max_length=50, null=True, choices=[
        ('course_created', 'Course Created'),
        ('course_updated', 'Course Updated'),
        ('course_deleted', 'Course Deleted'),
        ('lesson_created', 'Lesson Created'),
        ('lesson_updated', 'Lesson Updated'),
        ('lesson_deleted', 'Lesson Deleted'),
    ])

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'