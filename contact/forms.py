from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Your Message'}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise ValidationError("Name should not contain numbers.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.split()) < 2:
            raise ValidationError("Message should contain more than one word.")
        return message
