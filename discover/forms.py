from .models import Comment, Post, UserProfile
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'featured_image', 'excerpt', 'budget',
                  'currency', 'location', 'latitude', 'longitude', 'nights', 'people']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title of your post'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter a unique URL-friendly identifier'}),
            'content': SummernoteWidget(attrs={'placeholder': 'Write your post content here...'}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Enter a short summary of your post'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Enter the budget for this place'}),
            'currency': forms.Select(),
            'location': forms.TextInput(attrs={'placeholder': 'Enter the location'}),
            'latitude': forms.NumberInput(attrs={'placeholder': 'Enter the latitude'}),
            'longitude': forms.NumberInput(attrs={'placeholder': 'Enter the longitude'}),
            'nights': forms.NumberInput(attrs={'placeholder': 'Enter the number of nights'}),
            'people': forms.NumberInput(attrs={'placeholder': 'Enter the number of people'}),
        }


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
