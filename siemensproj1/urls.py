from django.urls import path
from . import views

urlpatterns = [
    path('bye/', views.say_hello),
    path('form/', views.upload_file)
]

