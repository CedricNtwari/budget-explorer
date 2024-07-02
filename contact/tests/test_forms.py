from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):
    """
    Test case for the ContactForm.

    This test case includes tests to verify the validation logic of the ContactForm.
    It checks for valid form submissions, invalid name submissions with numbers,
    and invalid message submissions with only one word.
    """

    def test_valid_form(self):
        """
        Test that a form with valid data is considered valid.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_name_with_number(self):
        """
        Test that a form with a name containing numbers is considered invalid.
        """
        form_data = {
            'name': 'John Doe1',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_invalid_message_with_one_word(self):
        """
        Test that a form with a message containing only one word is considered invalid.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Test'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)
