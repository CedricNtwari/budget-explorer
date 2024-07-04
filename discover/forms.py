from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms
from .models import Comment, Post, UserProfile
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
import os
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments on posts.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Enter your comment here...', 'required': True}),
        }


class PostForm(forms.ModelForm):
    """
    A form for creating and updating posts with fields for title, slug, content,
    featured image, excerpt, budget, currency, location, latitude, longitude,
    nights, and people.
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'featured_image', 'excerpt', 'budget',
                  'currency', 'location', 'latitude', 'longitude', 'nights', 'people']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title of your post', 'required': True}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter a unique URL-friendly identifier', 'required': True}),
            'content': SummernoteWidget(attrs={'placeholder': 'Write your post content here...', 'required': True}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Enter a short summary of your post', 'required': True}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Enter the budget for this place', 'required': True}),
            'currency': forms.Select(attrs={'required': True}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter the location', 'required': True}),
            'latitude': forms.NumberInput(attrs={'placeholder': 'Enter the latitude', 'required': True}),
            'longitude': forms.NumberInput(attrs={'placeholder': 'Enter the longitude', 'required': True}),
            'nights': forms.NumberInput(attrs={'placeholder': 'Enter the number of nights'}),
            'people': forms.NumberInput(attrs={'placeholder': 'Enter the number of people'}),
        }

    def clean_title(self):
        """
        Validate that the title contains only words and not numbers.
        """
        title = self.cleaned_data.get('title')
        if not all(x.isalpha() or x.isspace() for x in title):
            raise forms.ValidationError(
                "The title must contain words and not numbers.")
        return title

    def clean_budget(self):
        """
        Validate that the budget is a numeric value when the currency is Euro.
        """
        budget = self.cleaned_data.get('budget')
        currency = self.cleaned_data.get('currency')
        if currency == 'EUR' and not isinstance(budget, (int, float)):
            raise forms.ValidationError(
                "The budget must be a numeric value when the currency is Euro.")
        return budget

    def clean_slug(self):
        """
        Validate that the slug is unique.
        """
        slug = self.cleaned_data.get('slug')
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                "This slug is already in use. Please choose another.")
        return slug

    def clean_latitude(self):
        """
        Validate that the latitude is a numeric value.
        """
        latitude = self.cleaned_data.get('latitude')
        try:
            float(latitude)
        except ValueError:
            raise forms.ValidationError(
                "The latitude must be a numeric value.")
        return latitude

    def clean_longitude(self):
        """
        Validate that the longitude is a numeric value.
        """
        longitude = self.cleaned_data.get('longitude')
        try:
            float(longitude)
        except ValueError:
            raise forms.ValidationError(
                "The longitude must be a numeric value.")
        return longitude


class ProfilePictureForm(forms.ModelForm):
    """
    A form for uploading and updating a user's profile picture.
    """
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'required': True}),
        }

    def clean_profile_picture(self):
        """
        Validate that the uploaded file is an image with a valid extension.
        """
        picture = self.cleaned_data.get('profile_picture')
        if picture:
            ext = os.path.splitext(picture.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
            if ext not in valid_extensions:
                raise forms.ValidationError(
                    "Unsupported file extension. Allowed extensions are: .jpg, .jpeg, .png, .webp")
        return picture


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
