from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    """
    Form for users to contact the site administration.

    Fields:
    - name: The name of the user (max length: 100 characters, required).
    - email: The email address of the user (required).
    - message: The message from the user (required).
    """

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Your Name"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"placeholder": "Your Message"})
    )

    def clean_name(self):
        """
        Validate that the name field does not contain any numbers.

        Returns:
        - The cleaned name if valid.

        Raises:
        - ValidationError: If the name contains any numbers.
        """
        name = self.cleaned_data.get("name")
        if any(char.isdigit() for char in name):
            raise ValidationError("Name should not contain numbers.")
        return name

    def clean_message(self):
        """
        Validate that the message field contains more than one word.

        Returns:
        - The cleaned message if valid.

        Raises:
        - ValidationError: If the message contains fewer than two words.
        """
        message = self.cleaned_data.get("message")
        if len(message.split()) < 2:
            raise ValidationError("Message should contain more than one word.")
        return message
