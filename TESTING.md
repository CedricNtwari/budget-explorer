# Testing Documentation

## Overview

This document provides a detailed breakdown of the automated and manual tests performed on the "Budget Explorer" application. Each test case includes the expected behavior, testing steps, observed results, and any fixes applied.

### Automated Tests

#### About Page Tests

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
  ...

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
