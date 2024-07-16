# helloapp/urls.py
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),  # This maps the root URL of the app to the hello_world view
]
