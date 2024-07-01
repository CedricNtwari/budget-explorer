from django.test import TestCase
from django.urls import reverse
from discover.models import Post, Favorite
from django.contrib.auth.models import User


class FavoriteTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            budget=100,
            currency='EUR',
            location='Test Location',
            latitude=45.0,
            longitude=7.0,
            status=1
        )

    def test_add_favorite(self):
        response = self.client.get(
            reverse('add_favorite', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Favorite.objects.filter(
            user=self.user, post=self.post).exists())

    def test_remove_favorite(self):
        Favorite.objects.create(user=self.user, post=self.post)
        response = self.client.get(
            reverse('remove_favorite', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Favorite.objects.filter(
            user=self.user, post=self.post).exists())
