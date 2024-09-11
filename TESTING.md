# Testing Documentation

## Overview

This document provides a detailed breakdown of the automated and manual tests performed on the "Budget Explorer" application. Each test case includes the expected behavior, testing steps, observed results, and any fixes applied.

### About Page Tests

#### Automated Tests

1. **Test Case: About Page Loads Successfully**

   - **Expected**: The about page should load with a `200 OK` status when requested.
   - **Testing**: Accessed the about page via the `/about/` URL.
   - **Result**: Page loaded successfully with a `200 OK` status.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_about_me_view_status_code(self):
    response = self.client.get(reverse("about"))
    self.assertEqual(response.status_code, 200)
   ```

2. **Test Case: Correct Template Used for About Page**

- **Expected**: The correct template, `about.html`, should be used to render the about page.
- **Testing**: Checked that the `about.html` template was used.
- **Result**: The `about.html` template was used successfully.
- **Fix**: N/A (everything worked as expected).

  ```python
  def test_about_me_view_template_used(self):
   response = self.client.get(reverse("about"))
   self.assertTemplateUsed(response, "about/about.html")
  ```

3. **Test Case: About Page Content**

- **Expected**: The title and content from the About model should be rendered correctly on the page.
- **Testing**: We verified that the title and content of the About instance are present in the page's context and correctly rendered.
- **Result**: The title "About Me" and the content "This is some information about me" were correctly displayed on the page.
- **Fix**: N/A (everything worked as expected).

```python
  def test_about_me_view_context(self):
    response = self.client.get(reverse("about"))
    self.assertIn("about", response.context)
    self.assertEqual(response.context["about"].title, "About Me")
    self.assertEqual(response.context["about"].content, "This is some information about me.")
```

4. **Test Case: No About Entry Exists**

- **Expected**: If no About entry exists in the database, the page should still load but display no content.
- **Testing**: We deleted all About instances from the database and checked the response to ensure that the page loads without errors and handles the absence of content gracefully.
- **Result**: The page loaded successfully, but the about context was None, as expected.
- **Fix**: N/A (expected behavior).

```python
  def test_about_me_view_no_about_entry(self):
    About.objects.all().delete()
    response = self.client.get(reverse("about"))
    self.assertEqual(response.context["about"], None)
```

#### Manual Tests

1. Test Case: Image & Content Rendering

- **Expected**: The image (company logo) and the content on the about page should render properly.
- **Testing**: Visited the about page on Chrome, Firefox, and - Safari to verify that the image and content load correctly.
- **Result**: The image and content rendered correctly on all browsers.
- **Fix**: N/A (everything worked as expected).

2. Test Case: Mobile Responsiveness

- **Expected**: The application should adjust to smaller screen sizes without breaking the layout.
- **Testing**: Tested on Chrome's mobile view and real devices.
- **Result**: The layout adjusted correctly for mobile screens.
- **Fix**: N/A

3. Test Case: Browser Compatibility

- **Expected**: The application should function correctly across different browsers (Chrome, Firefox, Safari).
- **Testing**: Loaded the application in multiple browsers and tested interactive features.
- **Result**: The application worked as expected across all browsers.
- **Fix**: N/A

### Contact Page Tests

#### Automated Tests

1. **Test Case: About Page Loads Successfully**

   - **Expected**: The contact page should load with a `200 OK` status when requested.
   - **Testing**: Accessed the about page via the `/contact/` URL.
   - **Result**: Page loaded successfully with a `200 OK` status and used the `contact.html` template.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_get_contact_page(self):
    response = self.client.get(reverse("contact"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "contact/contact.html")
   ```

2. **Test Case: Valid Contact Form Submission**

- **Expected**: A valid contact form submission should redirect to the contact page with a success message, and an email should be sent.
- **Testing**: Submitted a valid contact form with the fields `name`, `email`, and `message` filled in correctly. Checked the recipient's inbox to confirm the email was received. Also logged into the Mailjet platform to confirm the email was successfully sent.
- **Result**: The form submission was successful, the page redirected, the email was received in the inbox, and the Mailjet dashboard confirmed the email was sent.
- **Fix**: N/A (everything worked as expected).

  ```python
  def test_post_valid_contact_form(self):
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

  ```

3. **Test Case: Invalid Contact Form Submission (Name Contains Numbers)**

- **Expected**: Submitting a form where the name contains numbers should trigger a validation error and the form should be re-rendered with error messages.
- **Testing**: Submitted a form with an invalid name containing numbers.
- **Result**: The form submission failed as expected, the page re-rendered, and the error "Name should not contain numbers" was displayed.
- **Fix**: N/A (everything worked as expected).

```python
  def test_invalid_name_with_number(self):
    form_data = {
        "name": "John Doe1",
        "email": "john.doe@example.com",
        "message": "This is a test message.",
    }
    response = self.client.post(reverse("contact"), data=form_data)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "contact/contact.html")
    self.assertContains(response, "Name should not contain numbers.")
```

4. **Test Case: Invalid Contact Form Submission (Message Too Short)**

- **Expected**: Submitting a form with a message containing only one word should trigger a validation error and the form should be re-rendered with error messages.
- **Testing**: Submitted a form where the message contained only one word.
- **Result**: The form submission failed, and the error "Message should contain more than one word" was displayed.
- **Fix**: N/A (expected behavior).

```python
 def test_invalid_message_with_one_word(self):
    form_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "message": "Test",
    }
    response = self.client.post(reverse("contact"), data=form_data)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "contact/contact.html")
    self.assertContains(response, "Message should contain more than one word.")

```

#### Manual Tests

1. Test Case: Form Field Validation on Contact Page

- **Expected**: Each field (name, email, message) should be validated correctly (e.g., name must not contain numbers, message must be longer than one word).
- **Testing**: Manually entered invalid data (e.g., name with numbers, message with one word) and verified that error messages appeared.
- **Result**: Validation errors were correctly displayed on the contact form for invalid data.
- **Fix**: N/A (everything worked as expected).

2. Test Case: Email Delivery

- **Expected**: The email should be delivered both to the inbox and logged in Mailjet.
- **Testing**: Filled out the form with valid details and checked the email inbox to verify that the email was sent.
- **Result**: The email was received successfully, and it was also visible on the Mailjet platform.
- **Fix**: N/A

3. Test Case: Browser Compatibility

- **Expected**: The contact form should work correctly across different browsers (Chrome, Firefox, Safari).
- **Testing**: Manually tested the contact form submission on multiple browsers to verify consistent functionality.
- **Result**: The form worked as expected on all tested browsers.
- **Fix**: N/A

4. Test Case: Mobile Responsiveness

- **Expected**: The contact form should be fully responsive and usable on mobile devices.
- **Testing**:Tested the contact form on mobile devices (using Chrome DevTools and real devices) to ensure the layout adjusted properly.
- **Result**: The form was responsive and functioned correctly on all devices.
- **Fix**: N/A

### Known Bugs

#### Email Verification 500 Server Error

- **Description**: During the registration process, users experience a 500 error when clicking on the email verification link.
- **Steps to Reproduce**:

1. Register a new user account.
2. Receive the verification email.
3. Click the verification link.

- **Expected**: The user should be redirected to the login page after email verification.
- **Observed**: A 500 server error occurs.
- **Fix**: Currently under investigation.

```

```
