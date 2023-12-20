from django.urls import path
from about import views

app_name = 'contact'

urlpatterns = [
    path('', views.about, name='about'),
]
