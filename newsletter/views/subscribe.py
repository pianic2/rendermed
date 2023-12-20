# views.py

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView

from newsletter.forms import SubscriberForm
from newsletter.models import Subscriber

class SubscribeView(FormView):
    template_name = 'newsletter/subscribe.html'
    form_class = SubscriberForm
    success_messages = 'You join ours newsletter'

    def form_valid(self, form):
        subscriber = form.save()
        return super().form_valid(form)

class UnsubscribeView(RedirectView):
    pattern_name = 'unsubscribe_success'

    def get_redirect_url(self, *args, **kwargs):
        email = kwargs.get('email')
        subscriber = Subscriber.objects.filter(email=email).first()
        if subscriber:
            subscriber.delete()
        return super().get_redirect_url(*args, **kwargs)
