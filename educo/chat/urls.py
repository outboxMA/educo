from django.urls import path
from .views import deepseek_page, call_deepseek

urlpatterns = [
    path("", deepseek_page, name="deepseek_page"),
    path("call/", call_deepseek, name="deepseek_api"),
]
