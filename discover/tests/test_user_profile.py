from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from discover.models import UserProfile
import os


class ProfilePictureFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user)

    def test_valid_image_upload(self):
        with open(os.path.join(os.path.dirname(__file__), 'test_image.jpg'), 'rb') as image:
            response = self.client.post(reverse('user_profile'), {
                                        'profile_picture': image})
            self.assertEqual(response.status_code, 302)
            self.profile.refresh_from_db()
            self.assertTrue(self.profile.profile_picture)

    def test_invalid_image_extension(self):
        with open(os.path.join(os.path.dirname(__file__), 'test_document.txt'), 'rb') as doc:
            response = self.client.post(reverse('user_profile'), {
                                        'profile_picture': doc})
            self.assertEqual(response.status_code, 200)
            form = response.context['form']
            self.assertIn('profile_picture', form.errors)
