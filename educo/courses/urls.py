from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('toggle-status/<int:course_id>/', views.toggle_course_status, name='toggle_course_status'),
    path('session/edit/<int:session_id>/', views.edit_session, name='edit_session'),  
    path('session/delete/<int:session_id>/', views.delete_session, name='delete_session'),  
]
