from django.test import TestCase
from django.urls import reverse
from discover.models import Post
from django.contrib.auth.models import User


class PostTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass", is_staff=True
        )
        self.client.login(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.user,
            content="Test content",
            budget=100,
            currency="EUR",
            location="Test Location",
            latitude=45.0,
            longitude=7.0,
            status=1,
        )

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_add_post_view(self):
        response = self.client.get(reverse("add_post"))
        self.assertEqual(response.status_code, 200)

    def test_add_post(self):
        data = {
            "title": "New Post",
            "slug": "new-post",
            "content": "New content",
            "featured_image": "",  # Assuming no image is uploaded
            "excerpt": "New excerpt",
            "budget": 150,
            "currency": "EUR",
            "location": "New Location",
            "latitude": 46.0,
            "longitude": 6.0,
            "nights": 2,
            "people": 4,
            "status": 1,
        }
        response = self.client.post(reverse("add_post"), data)
        # Expecting a redirect after successful post creation
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(slug="new-post").exists())
