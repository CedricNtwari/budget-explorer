from django.test import TestCase
from .forms import PostForm, ProfilePictureForm, CommentForm
from .models import Post, UserProfile, Comment
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class PostFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.valid_data = {
            'title': 'Test Post',
            'slug': 'test-post',
            'content': 'This is a test post content.',
            'excerpt': 'This is an excerpt.',
            'budget': 100.00,
            'currency': 'EUR',
            'location': 'Test Location',
            'latitude': 10.123456,
            'longitude': 20.123456,
            'nights': 2,
            'people': 4
        }

    def test_valid_post_form(self):
        form = PostForm(data=self.valid_data)
        if not form.is_valid():
            print("Form errors:", form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_title(self):
        data = self.valid_data.copy()
        data['title'] = '1234'
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_duplicate_slug(self):
        Post.objects.create(author=self.user, **self.valid_data)
        form = PostForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors)

    def test_invalid_budget_with_currency(self):
        data = self.valid_data.copy()
        data['budget'] = 'abc'
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('budget', form.errors)

    def test_invalid_latitude(self):
        data = self.valid_data.copy()
        data['latitude'] = 'abc'
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('latitude', form.errors)

    def test_invalid_longitude(self):
        data = self.valid_data.copy()
        data['longitude'] = 'abc'
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('longitude', form.errors)


class ProfilePictureFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_valid_image_upload(self):
        with open(os.path.join(os.path.dirname(__file__), 'test_image.jpg'), 'rb') as image:
            form = ProfilePictureForm(data={}, files={'profile_picture': SimpleUploadedFile(
                image.name, image.read(), content_type='image/jpeg')})
            self.assertTrue(form.is_valid())

    def test_invalid_image_extension(self):
        with open(os.path.join(os.path.dirname(__file__), 'test_document.txt'), 'rb') as doc:
            form = ProfilePictureForm(data={}, files={'profile_picture': SimpleUploadedFile(
                doc.name, doc.read(), content_type='text/plain')})
            self.assertFalse(form.is_valid())
            self.assertIn('profile_picture', form.errors)


class CommentFormTest(TestCase):

    def test_valid_comment(self):
        form = CommentForm(data={'body': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_empty_comment(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors)
