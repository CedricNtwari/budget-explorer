from django.test import TestCase
from django.urls import reverse
from discover.models import Post, Comment
from django.contrib.auth.models import User


class CommentTests(TestCase):

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
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Test comment'
        )

    def test_comment_on_post(self):
        data = {
            'body': 'New comment'
        }
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Comment submitted successfully.')

    def test_edit_comment(self):
        data = {
            'body': 'Edited comment'
        }
        response = self.client.post(
            reverse('comment_edit', args=[self.post.slug, self.comment.id]), data)
        # Redirect after successful edit
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Edited comment')

    def test_delete_comment(self):
        response = self.client.post(
            reverse('comment_delete', args=[self.post.slug, self.comment.id]))
        # Redirect after successful delete
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
