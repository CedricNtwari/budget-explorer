from django.test import TestCase
from django.urls import reverse
from .models import About


class AboutMeViewTests(TestCase):
    def setUp(self):
        About.objects.create(
            title="About Me",
            content="This is some information about me.",
            updated_on="2024-07-01"
        )

    def test_about_me_view_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_me_view_template_used(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_me_view_context(self):
        response = self.client.get(reverse('about'))
        self.assertIn('about', response.context)
        self.assertEqual(response.context['about'].title, "About Me")

    def test_about_me_view_no_about_entry(self):
        About.objects.all().delete()
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context['about'], None)
