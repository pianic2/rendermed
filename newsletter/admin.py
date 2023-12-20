from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from newsletter.views import admin_views
from newsletter.models import *
from newsletter.forms import *
from django import forms
from django.shortcuts import render
from django.conf import settings
# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Subscriber)
admin.site.register(Template)

class NewsletterAdminSite(admin.AdminSite):
    site_header = 'Newsletter Admin'
    site_title = 'Newsletter Admin Portal'
    index_title = 'Welcome to Newsletter Portal'
    index_template = 'newsletter-admin/app_index.html'
    app_index_template = 'newsletter-admin/app_index.html'

    def get_urls(self):
        return [
            path("", self.admin_view(self.newsletter_view)),
            path("newsletter/", self.admin_view(self.newsletter_view)),
            *super().get_urls(),
        ]

    def newsletter_view(self, request, *args, **kwargs):
        if request.method == 'POST':
            templateSend = TemplateSelectForm(request.POST)
            if templateSend.is_valid():
                try:
                    template = Template.objects.filter(title=templateSend.cleaned_data['templates'].get())
                except:
                    template = None
                context = dict(
                    self.each_context(request),
                    settings = settings,
                    adminform = {
                        'newsletterAdd': NewsletterContentForm,
                        'subscriberSelect': SubscriberSelectForm,
                        'templateSend': templateSend
                        },
                    template = template,
                    )
                print()
                return render(request, 'newsletter-admin/app_index.html', context)
        templateSend = TemplateSelectForm()
        context = dict(
            # Include common variables for rendering the admin template.
            self.each_context(request),
            # Anything else you want in the context...
            settings = settings,
            adminform = {
                'newsletterAdd': NewsletterContentForm,
                'subscriberSelect': SubscriberSelectForm,
                'templateSend': templateSend
                },
            )
        return render(request, 'newsletter-admin/app_index.html', context)


newsletter_admin_site = NewsletterAdminSite(name='newsletter_admin')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),)
    add_form_template = 'newsletter-admin/newsletter_add.html'

    def get_urls(self):
        return [
            path("<slug>/detail", self.admin_site.admin_view(admin_views.NewsletterDetailView.as_view()), name=f"newsletter_newsletter_detail",),
            path("add", self.admin_site.admin_view(admin_views.NewsletterAddView.as_view()), name=f"newsletter_newsletter_add",),
            path("send", self.admin_site.admin_view(admin_views.NewsletterSendView.as_view()), name=f"newsletter_newsletter_send",),
            *super().get_urls(),
        ]

    def add(self, obj: Newsletter) -> str:
        url = reverse("newsletter_admin:newsletter_newsletter_add", args=[obj.slug])
        return format_html(f'<a href="{url}">📝</a>')

    def detail(self, obj: Newsletter) -> str:
        url = reverse("newsletter_admin:newsletter_newsletter_detail", args=[obj.slug])
        return format_html(f'<a href="{url}">📝</a>')

newsletter_admin_site.register(Newsletter, NewsletterAdmin)
newsletter_admin_site.register(Subscriber)
newsletter_admin_site.register(Template)
