from django.urls import path
from home import views

urlpatterns = [
    path('', views.landing, name='landing'),
]
