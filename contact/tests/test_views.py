from django.urls import reverse
from django.test import TestCase
from django.core import mail


class ContactViewTest(TestCase):

    def test_get_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_post_valid_contact_form(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('contact'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Message from John Doe')

    def test_post_invalid_contact_form(self):
        form_data = {
            'name': 'John Doe1',
            'email': 'john.doe@example.com',
            'message': 'Test'
        }
        response = self.client.post(reverse('contact'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertContains(response, "Name should not contain numbers.")
        self.assertContains(
            response, "Message should contain more than one word.")
        self.assertEqual(len(mail.outbox), 0)
