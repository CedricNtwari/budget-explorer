from django.test import TestCase
from django.urls import reverse
from .models import About


class AboutMeViewTests(TestCase):
    def setUp(self):
        """
        Set up a sample About instance for testing.
        """
        About.objects.create(
            title="About Me",
            content="This is some information about me.",
            updated_on="2024-07-01"
        )

    def test_about_me_view_status_code(self):
        """
        Test that the About Me view returns a 200 status code.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_me_view_template_used(self):
        """
        Test that the About Me view uses the correct template.
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_me_view_context(self):
        """
        Test that the About Me view provides the correct context.
        """
        response = self.client.get(reverse('about'))
        self.assertIn('about', response.context)
        self.assertEqual(response.context['about'].title, "About Me")

    def test_about_me_view_no_about_entry(self):
        """
        Test the behavior of the About Me view when no About instance exists.
        """
        About.objects.all().delete()
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context['about'], None)
