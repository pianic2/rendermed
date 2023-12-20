from django.urls import path
from newsletter.views import subscribe

app_name = 'newsletter'

urlpatterns = [
    path('', subscribe.UnsubscribeView.as_view(), name='newsletter'),
    path('subscribe/', subscribe.SubscribeView.as_view(), name='subscribe'),
]
