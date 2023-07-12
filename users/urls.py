
from django.contrib import admin
from django.urls import path, include

from .views import RegisterUserView
urlpatterns = [
    # path("users/" , )
    path("register" , view=RegisterUserView.as_view(), name="register_view" )    
]
