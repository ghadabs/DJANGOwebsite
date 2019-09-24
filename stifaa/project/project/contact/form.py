from django import forms
from .models import NewsletterUser

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class NewsletterUserForm(forms.ModelForm):
    class Meta:
        model=NewsletterUser
        fields=['email']

        def clean_mail(self):
            email=self.cleaned_data.get('email')

            return email


