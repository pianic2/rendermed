from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from newsletter.models import *
from newsletter.forms import *
from newsletter import admin


class NewsletterDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "newsletter.view_newsletter"
    template_name = "newsletter-admin/folder_detail.html"
    model = Newsletter

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.newsletter_admin_site.each_context(self.request),
            "opts": self.model._meta,
        }

class NewsletterAddView(PermissionRequiredMixin, CreateView):
    permission_required = "newsletter.view_newsletter"
    template_name = "newsletter-admin/newsletter_add.html"
    model = Newsletter
    form_class = NewsletterContentForm
    success_message = 'Success: Book was created.'

    def get_context_data(self, **kwargs):
        context = {
            **super().get_context_data(**kwargs),
            **admin.newsletter_admin_site.each_context(self.request),
            "opts": self.model._meta,
        }
        return context


class NewsletterSendView(PermissionRequiredMixin, View):
    permission_required = "newsletter.view_newsletter"
    template_name = 'newsletter-admin/newsletter_send.html'
    success_message = 'Success: Book was created.'
    success_url = 'newsletter_admin:index'
    
    def get(self, request, *args, **kwargs):
        form = SubscriberSelectForm()
        return render(request, self.template_name, {'adminform': {'sendform':form}})

    def get_context_data(self, **kwargs):
        context = {
            **super().get_context_data(**kwargs),
            **admin.newsletter_admin_site.each_context(self.request),
            "opts": self.model._meta,
        }
        return context
