from django.urls import reverse
from django.test import TestCase
from django.core import mail


class ContactViewTest(TestCase):
    """
    Test case for the contact view.

    This test case includes tests to verify the behavior of the contact view.
    It checks for the correct rendering of the contact page, handling of valid
    and invalid form submissions, and email sending functionality.
    """

    def test_get_contact_page(self):
        """
        Test that the contact page is rendered correctly with a 200 status code
        and the correct template is used.
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_post_valid_contact_form(self):
        """
        Test that a valid form submission redirects correctly and sends an email.
        """
        form_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse("contact"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("contact"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Message from John Doe")

    def test_post_invalid_contact_form(self):
        """
        Test that an invalid form submission re-renders the contact page with
        errors and does not send an email.
        """
        form_data = {
            "name": "John Doe1",
            "email": "john.doe@example.com",
            "message": "Test",
        }
        response = self.client.post(reverse("contact"), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertContains(response, "Name should not contain numbers.")
        self.assertContains(response, "Message should contain more than one word.")
        self.assertEqual(len(mail.outbox), 0)
