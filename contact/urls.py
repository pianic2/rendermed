from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('contact', views.contact, name='contact'),
]
