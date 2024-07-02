from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_name_with_number(self):
        form_data = {
            'name': 'John Doe1',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_invalid_message_with_one_word(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Test'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)
