from django import forms
from newsletter.models import *

class NewsletterContentForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'autocomplete': 'off',
                'aria-label': 'title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'autocomplete': 'off',
                'aria-label': 'content',
                }),
        }

class SubscriberSelectForm(forms.Form):
    subscribers = forms.ModelMultipleChoiceField(
        queryset=Subscriber.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            #'class': 'form-check-input',
            #'type': 'checkbox',
        }),
    )

    def clean(self):
        cleaned_data = super().clean()
        subscribers = cleaned_data.get('subscribers')
        if not subscribers:
            raise forms.ValidationError('Please select at least one subscriber.')
        return cleaned_data

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'autocomplete': 'off',
                'aria-label': 'Email Address',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''

class TemplateSelectForm(forms.Form):
    templates = forms.ModelMultipleChoiceField(
        queryset=Template.objects.all(),
    )

    def clean(self):
        cleaned_data = super().clean()
        templates = cleaned_data.get('templates')
        if not templates:
            raise forms.ValidationError('Please select at least one template.')
        return cleaned_data
