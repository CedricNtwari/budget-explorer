# Testing Documentation

## Overview

This document provides a detailed breakdown of the automated and manual tests performed on the "Budget Explorer" application. Each test case includes the expected behavior, testing steps, observed results, and any fixes applied.

### About Page Tests

#### Automated Tests

1. **Test Case: About Page Loads Successfully**

   - **Expected**: The About page should load with a `200 OK` status when requested.
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
   - **Testing**: Submitted a form in which the message contained only one word.
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

   - **Expected**: Each field (name, email, message) should be validated correctly (e.g., the name must not contain numbers, and the message must be longer than one word).
   - **Testing**: Manually entered invalid data (e.g., a name with numbers or a message with only one word) and verified that error messages were displayed.
   - **Result**: Validation errors were correctly displayed on the contact form for invalid data.
   - **Fix**: N/A (everything worked as expected).

2. Test Case: Email Delivery

   - **Expected**: The email should be delivered both to the inbox and logged in Mailjet.
   - **Testing**: Filled out the form with valid details and checked the email inbox to verify that the email was sent.
   - **Result**: The email was received successfully, and it was also visible on the Mailjet platform.
   - **Fix**: N/A

3. Test Case: Browser Compatibility

   - **Expected**: The contact form should work correctly across different browsers (Chrome, Firefox, Safari).
   - **Testing**: Tested the contact form on multiple browsers to ensure consistent functionality.
   - **Result**: The form worked as expected on all tested browsers.
   - **Fix**: N/A

4. Test Case: Mobile Responsiveness

   - **Expected**: The contact form should be fully responsive and usable on mobile devices.
   - **Testing**:Tested the contact form on mobile devices (using Chrome DevTools and real devices) to ensure the layout adjusted properly.
   - **Result**: The form was responsive and functioned correctly on all devices.
   - **Fix**: N/A

### Comment Tests

#### Automated Tests

1. **Test Case: Comment on a Post**

   - **Expected**: A user should be able to submit a comment on a post. Upon submission, the comment should be saved, and the page should reload with a success message.
   - **Testing**: Logged in as a user, posted a comment on the post.
   - **Result**: The comment was submitted successfully, and the message "Comment submitted successfully." was displayed.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_comment_on_post(self):
    data = {"body": "New comment"}
    response = self.client.post(reverse("post_detail", args=[self.post.slug]), data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Comment submitted successfully.")
   ```

2. **Test Case: Edit a Comment**

   - **Expected**: A user should be able to edit their own comment, and the updated comment should be saved and visible.
   - **Testing**: Edited an existing comment on the post.
   - **Result**: The comment was updated successfully, and the page redirected after the edit.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_edit_comment(self):
   data = {"body": "Edited comment"}
   response = self.client.post(
      reverse("comment_edit", args=[self.post.slug, self.comment.id]), data
   )
   self.assertEqual(response.status_code, 302)
   self.comment.refresh_from_db()
   self.assertEqual(self.comment.body, "Edited comment")
   ```

3. **Test Case: Delete a Comment**

   - **Expected**: A user should be able to delete their own comment, and the comment should be removed from the database.
   - **Testing**: Deleted an existing comment.
   - **Result**: The comment was deleted successfully, and the page redirected after the deletion.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_delete_comment(self):
    response = self.client.post(
        reverse("comment_delete", args=[self.post.slug, self.comment.id])
    )
    self.assertEqual(response.status_code, 302)
    self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
   ```

### Favorite Tests

#### Automated Tests

1. **Test Case: Add a Post to Favorites**

   - **Expected**: A user should be able to mark a post as a favorite, and the post should be added to their favorites list.
   - **Testing**: Added a post to favorites.
   - **Result**: The post was added to favorites, and the user was redirected to the post detail page.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_add_favorite(self):
    response = self.client.get(reverse("add_favorite", args=[self.post.slug]))
    self.assertEqual(response.status_code, 302)
    self.assertTrue(Favorite.objects.filter(user=self.user, post=self.post).exists())

   ```

2. **Test Case: Remove a Post from Favorites**

   - **Expected**: A user should be able to remove a post from their favorites list.
   - **Testing**: Removed a post from favorites.
   - **Result**: The post was removed from favorites, and the user was redirected to the post detail page.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_remove_favorite(self):
    Favorite.objects.create(user=self.user, post=self.post)
    response = self.client.get(reverse("remove_favorite", args=[self.post.slug]))
    self.assertEqual(response.status_code, 302)
    self.assertFalse(Favorite.objects.filter(user=self.user, post=self.post).exists())

   ```

### Post Tests

#### Automated Tests

1. **Test Case: Post List View**

   - **Expected**:The post list page should load successfully and display all published posts.
   - **Testing**: Accessed the home page and checked if the post title was displayed.
   - **Result**: The post was displayed on the post list page.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_post_list_view(self):
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.post.title)
   ```

2. **Test Case: Post Detail View**

   - **Expected**: The post detail page should load successfully and display the post content.
   - **Testing**: Accessed the post detail page and checked if the post title and content were displayed.
   - **Result**: The post content was displayed correctly on the post detail page.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_post_detail_view(self):
    response = self.client.get(reverse("post_detail", args=[self.post.slug]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.post.title)
   ```

3. **Test Case: Add a New Post**

   - **Expected**: A user with staff permissions should be able to add a new post.
   - **Testing**: Submitted a new post form.
   - **Result**: The post was created successfully, and the user was redirected.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_add_post(self):
    data = {
        "title": "New Post",
        "slug": "new-post",
        "content": "New content",
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
    self.assertEqual(response.status_code, 302)
    self.assertTrue(Post.objects.filter(slug="new-post").exists())
   ```

### User Profile Tests

#### Automated Tests

1. **Test Case: Valid Profile Picture Upload**

   - **Expected**:A user should be able to upload a valid profile picture with a supported extension.
   - **Testing**: Uploaded a valid image file as the profile picture.
   - **Result**: The profile picture was uploaded successfully, and the user was redirected.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_valid_image_upload(self):
    with open(os.path.join(os.path.dirname(__file__), "test_image.jpg"), "rb") as image:
        response = self.client.post(reverse("user_profile"), {"profile_picture": image})
        self.assertEqual(response.status_code, 302)
        self.profile.refresh_from_db()
        self.assertTrue(self.profile.profile_picture)
   ```

2. **Test Case: Invalid Profile Picture Upload**

   - **Expected**: If a user tries to upload a file with an invalid extension, an error message should be displayed.
   - **Testing**: Uploaded an invalid file (e.g., a .txt file) as the profile picture.
   - **Result**: The form submission failed, and an error message was displayed.
   - **Fix**: N/A (everything worked as expected).

   ```python
   def test_invalid_image_extension(self):
    with open(os.path.join(os.path.dirname(__file__), "test_document.txt"), "rb") as doc:
        response = self.client.post(reverse("user_profile"), {"profile_picture": doc})
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("profile_picture", form.errors)
   ```

#### Manual Tests

1. **Test Case: Post List Pagination**

   - **Expected**: The post list should display paginated posts, with navigation controls to view more posts.

   - **Testing**: Manually navigated through the post list pages to verify the pagination controls and ensure that the posts were displayed correctly.

   - **Result**: Pagination worked as expected, displaying the correct number of posts per page.

   - **Fix**: N/A (everything worked as expected).

2. **Test Case: Map Rendering**

   - **Expected**: The map should render properly on the post list and detail pages, displaying the locations of the posts.

   - **Testing**: Manually opened the map to check if the locations were marked correctly.

   - **Result**: The map and location markers were displayed correctly.

   - **Fix**: N/A (everything worked as expected).

3. **Test Case: Mobile Responsiveness**

   - **Expected**: The Discover page should adjust its layout and elements (like the map, posts, and forms) to fit smaller screen sizes without breaking the design.

   - **Testing**: Tested the Discover page on mobile devices and Chrome DevTools (mobile view) to ensure proper layout and functionality on smaller screens.

   - **Result**: The page was responsive and displayed correctly on mobile devices.

   - **Fix**: N/A (everything worked as expected).

4. **Test Case: Browser Compatibility**

   - **Expected**: The Discover page should work correctly across different browsers (e.g., Chrome, Firefox, Safari).
   - **Testing**: Opened the Discover page in multiple browsers to verify that all features (such as the map, forms, and pagination) worked as expected.
   - **Result**: The page functioned correctly across all tested browsers.
   - **Fix**: N/A (everything worked as expected).

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
