# students/urls.py

from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('<int:student_id>/edit/', views.student_edit, name='student_edit'),
    # path('<int:student_id>/enrollments/', views.enrollment_list, name='enrollments'),
    # path('<int:student_id>/enrollments/create/', views.enrollment_create, name='enrollment_create'),
    # path('enrollments/<int:enrollment_id>/edit/', views.enrollment_edit, name='enrollment_edit'),
    # path('enrollments/<int:enrollment_id>/delete/', views.enrollment_delete, name='enrollment_delete'),
]
