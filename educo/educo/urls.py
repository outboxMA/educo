from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('instructors/', include('instructors.urls')),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('chat/', include('chat.urls')),
    path('', include('core.urls')),
]
