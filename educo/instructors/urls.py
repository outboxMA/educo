from django.urls import path
from . import views

app_name = 'instructors'

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
    path('instructor/<int:pk>/', views.instructor_detail, name='instructor_detail'),
    path('instructor/add/', views.instructor_add, name='instructor_add'),
    path('instructor/edit/<int:pk>/', views.instructor_edit, name='instructor_edit'),
    path('instructor/delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
]
