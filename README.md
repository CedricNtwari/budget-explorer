## Budget Explorer

"Budget Explorer" is a full-stack web application designed to help users find and share budget-friendly places to visit within a specified budget. Users can enter their budget, location, and number of people, and the application returns a list of recommended places that meet their criteria. Users can also save their favorite places, view them on a map, and share their experiences with others.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Implementation Details](#implementation-details)
4. [Design Process](#design-process)
5. [User Stories and Agile Methodology](#user-stories-and-agile-methodology)
6. [Database Schema](#database-schema)

## Project Overview

This project was inspired by my wife’s experience when she first moved to Switzerland. She faced challenges browsing the internet to find budget-friendly places to visit. **Budget Explorer** is designed to make this easier for anyone moving to a new country or simply looking to explore their surroundings on a budget. The goal is to help users connect with their new environment and discover affordable adventures.

## Key Features

1. **User Authentication and Role-Based Access:**

   - User registration and login via email [Mailjet](https://app.mailjet.com/)
   - Users can log in using social platforms like Google and Facebook.
   - Role-based access control (e.g., regular users vs. admin).

![User Authentication](/static/images/authentication-.png)
![User Authentication](/static/images/authentication..png)

2. **Search, Filter and near me:**

   - Users can input their location, budget range, and number of people.
   - The application provides a list of places that fit the user's criteria.
   - Advanced filters like type of place, post title, or location.
   - Users can filter posts to find them easily by title or location.
   - The posts listing page updates to display only the posts that match the selected filters.
   - "Near me" feature to filter places within a certain distance from the user's current location.

![Search, Filter and near me](/static/images/search.png)

3. **Favorites:**

   - Users can save favorite places for easy access.

![Favorites](/static/images/favorite.png)

4. **Map Integration:**

   - Interactive map displaying the locations of recommended places.
   - Map view to explore places without leaving the site.
   - Focus on User Experience (UX) and Accessibility.

![Map Integration](/static/images/map.png)

5. **Intuitive and responsive design.**

   - Clear feedback on user actions (e.g., adding to favorites, leave a comment, users can update their infos).

![Intuitive and responsive design](/static/images/Intuitive.png)
![users can update their infos](/static/images/user.png)

## Implementation Details

1.  **Frontend:**

    - **Technologies:** HTML, CSS, Bootstrap for responsiveness and JavaScript for interactivity.

    - **Templates:** Django templates are used to render dynamic content .

2.  **Backend:**

    - **Technologies:** Python with Django for handling backend logic, authentication, and database management.

3.  **Database:**

    - **Database:** Relational database: PostgreSQL.
    - **Django ORM:** Used to define models for users, places, reviews, favorites, etc.

4.  **Map Integration:**

    - Google Maps API is used to display locations on an interactive map.

5.  **Testing:**

    5.1. **Automated Testing**:

    - Unit tests cover key features such as user authentication, CRUD operations, and search functionality.

    - Both "happy flow" (success) and "bad flow" (failure/error cases) are tested.

    - Django’s testing framework is used to ensure core functionalities behave as expected.

    5.2. **Manual Testing**:

    - The application was manually tested for responsiveness and usability across different browsers (Chrome, Firefox, Safari) and devices (mobile and desktop).
    - Manual tests were conducted to ensure the functionality of interactive elements, such as form submissions and navigation.

    5.3. **Test Coverage**:

    - **Unit Tests:** Key components such as views, models, and forms are tested.
    - **Integration Tests:** Ensure that different system components work together correctly, such as user authentication, data handling, and map integration.
    - **User Interface (UI) Tests:** Ensure the application renders correctly on various devices and screen sizes.

    For detailed test results,refer to the [TESTING.md](./TESTING.md) file.

6.  **Version Control:** Git, GitHub

7.  **Deployment to Heroku:**

    The application is deployed to Heroku, and here are the steps to set up the project:

    7.1. **Set Up a Heroku Account:**

    - Create an account at at [Heroku](https://signup.heroku.com/). - Optionally, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).


    7.2. **Create a new Heroku App:**

    - Log in to Heroku and create a new app.
    - Choose a unique name and select a region (United States or Europe).

    7.3. **Set Up External PostgreSQL Database:**

    - If you're using an external PostgreSQL database instead of Heroku’s built-in Postgres add-on, follow these steps:

    - Ensure that you have the PostgreSQL database already set up with the necessary credentials (host, database name, username, and password).
    - In your **env.py**, set the **DATABASE_URL** to the correct connection string.

    - You do not need to add the Heroku Postgres add-on in this case, but you must set the DATABASE_URL environment variable in Heroku’s Config Vars (Step 7.5).

    7.4. **Connect Your App to GitHub:**

    - In the Deploy tab on Heroku, select GitHub as your deployment method and connect your GitHub repository.

    7.5. **Set Environment Variables:**

    Set all environment variables in Heroku.

    - Go to the **Settings** tab in Heroku & Click **Reveal Config Vars** and add the following variables:

    ```
    DATABASE_URL=your_database_url
    SECRET_KEY=your_secret_key
    CLOUDINARY_URL=your_cloudinary_url
    MAILJET_API_KEY=your_mailjet_api_key
    MAILJET_API_SECRET=your_mailjet_api_secret
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    GOOGLE_MAPS_MAP_ID=your_google_maps_map_id
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    PROD_GOOGLE_REDIRECT_URI=https://<your-app-name>.herokuapp.com/accounts/google/login/callback/
    FACEBOOK_APP_ID=your_facebook_app_id
    FACEBOOK_APP_SECRET=your_facebook_app_secret
    PROD_FACEBOOK_REDIRECT_URI=https://<your-app-name>.herokuapp.com/accounts/facebook/login/callback/
    ENVIRONMENT=production
    DEBUG=False
    ```

    7.6. **Prepare the Application for Deployment:**

    - Ensure you have a Procfile that tells Heroku how to run your app

    ```
    web: gunicorn app_name.wsgi
    ```

    - Update your **requirements.txt** file by running:

    ```
    pip freeze > requirements.txt
    ```

    - Heroku doesn't serve static files by default. Configure your **settings.py**:

    ```
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```

    - Ensure your migrations are up to date:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    7.7.**Deploy the Application:**

    - In the **Deploy** tab on Heroku, select the branch to deploy and click **Deploy Branch**.

    7.8.**Create a Superuser (Optional):**

    -To access the Django admin panel, create a **superuser**:

    ```
    heroku run python manage.py createsuperuser
    ```

    7.9.**Open Your App:**

   - Visit app at:

    ```
    https://<your-app-name>.herokuapp.com
    ```


The application is deployed on Heroku: Budget Explorer on [Heroku](https://budget-explorer-b9fdc935d3db.herokuapp.com/).

### Example Blog Post Data for testing purposes

To add a new blog post, you can use the following JSON structure as an example. This example showcases a post about visiting Kyoto, Japan:

```json
{
  "model": "discover.post",
  "pk": null,
  "fields": {
    "title": "Discovering the Wonders of Kyoto",
    "slug": "discovering-the-wonders-of-kyoto",
    "author": 3,
    "content": "<p>Kyoto, the cultural heart of Japan, is renowned for its classical Buddhist temples, as well as gardens, imperial palaces, Shinto shrines, and traditional wooden houses. Here are some highlights to explore in this enchanting city.</p><p><b>Fushimi Inari Shrine</b></p><p>The Fushimi Inari Shrine is famous for its thousands of vermilion torii gates, which straddle a network of trails behind its main buildings. This shrine is dedicated to Inari, the Shinto god of rice, and offers a mesmerizing and spiritual experience.</p><p><b>Arashiyama Bamboo Grove</b></p><p>Walking through the Arashiyama Bamboo Grove feels like stepping into another world. The towering bamboo stalks provide a serene and magical atmosphere, perfect for a peaceful stroll.</p><p><b>Kinkaku-ji (Golden Pavilion)</b></p><p>Kinkaku-ji, or the Golden Pavilion, is one of Kyoto's most iconic landmarks. This Zen Buddhist temple is covered in gold leaf and reflects beautifully in the surrounding pond, making it a must-visit for anyone in Kyoto.</p>",
    "created_on": "2023-09-12T14:20:45.238Z",
    "status": 1,
    "excerpt": "Experience the cultural richness of Kyoto, from the spiritual Fushimi Inari Shrine to the serene Arashiyama Bamboo Grove and the iconic Kinkaku-ji.",
    "updated_on": "2023-09-25T11:30:56.217Z",
    "budget": 400.0,
    "currency": "JPY",
    "location": "Kyoto, Japan",
    "latitude": 35.0116,
    "longitude": 135.7681,
    "nights": 5,
    "people": 2
  }
}
```

## Design Process

The design of "Budget Explorer" is centered around providing a simple and intuitive user experience for individuals who are looking for budget-friendly travel destinations. The core design goals were:

1. **Simplicity**: The user interface is designed to be easy to navigate, with minimal distractions. The goal was to allow users to input information quickly and get the results they need without unnecessary complexity.

2. **Responsiveness**: Since users might access the platform from various devices, a responsive design was key. The layout adapts to different screen sizes, ensuring that the user experience remains consistent on desktop, tablet, and mobile devices.

3. **Visual Appeal**: The color scheme and typography were chosen to create a clean and professional look. The use of images, especially in the recommendations and map sections, was emphasized to make the experience more engaging.

4. **User Flow**: The main user journey, from entering budget information to viewing travel recommendations and saving favorites, was mapped out to ensure a logical and smooth progression.

5. **Mobile-First Approach**: By focusing on mobile usability first, the interface delivers a consistent experience across devices. The application was designed with mobile users in mind, ensuring a responsive design that adapts seamlessly from mobile phones to tablets and desktop screens.

6. **Wireframes**: During the early stages of development, wireframes were created for key pages, including the homepage, about page, contact page, sign-up, and login pages. These wireframes were designed for desktop, tablet, and mobile views to ensure responsiveness and usability.

[View Budget Explorer Design on Figma](https://www.figma.com/design/slFAyq0SK0UxFEt3CM2g7H/Budget-Explorer?node-id=0-1&node-type=canvas&t=qGdoeZAT4Pk8XC0G-0)

### Color Palette

The chosen color palette reflects the goal of creating a clean, professional, and visually appealing interface. The following colors were used:

- **Primary Color:** #188181
- **Secondary Color:** #FAC34F
- **Background Color:** #F9FAFC
- **Text Color:** #212529

## User Stories and Agile Methodology

- Defined epics and broke them down into user stories and tasks.
- Track project progress, GitHub Projects: <a href="https://github.com/users/CedricNtwari/projects/3/views/1" target="_blank">Project Board</a>

## Database Schema

**Data Model:**

A textual representation of the ERD

![A Entity-Relationship Diagram](/static/images/model-diagram.png)

**User Journey:**

A textual representation of the flowchart

![A description of the typical user flow through the app](/static/images/flowchart.png)

### Validator Testing

- HTML

  - No errors were returned when passing the source code viewed in the browser through the official [W3C validator](https://validator.w3.org/nu/#textarea)

  ![No errors html validator](/static/images/html.png)

- CSS

  - No errors were returned when passing the source code viewed in the browser through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

  ![No errors css validator](/static/images/js.png)

- Accessibility:
  - The accessibility score is high enough when passing through web dev tool Lighthouse
- JavaScript:
  - No errors were found when passing through the official [(Jshint) validator](https://jshint.com/)
- **Python**:
  - No issues were found when passing through the official [Black](https://black.readthedocs.io/en/stable/), Checked and formatted all python files
  - Results:
    `plaintext
reformatted /Users/cedric/budget-explorer/discover/models.py
reformatted /Users/cedric/budget-explorer/discover/forms.py
reformatted /Users/cedric/budget-explorer/discover/views.py
...
All done! ✨ 🍰 ✨
31 files reformatted, 12 files left unchanged.
`
    ![Python](/static/images/black.png)
- **Lighthouse**:

  - Tested with [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance, accessibility, best practices, and SEO.

  ![Lighthouse](/static/images/mobile.png)
  ![Lighthouse](/static/images/desktop.png)

### HTTPS Warnings Explanation

- **Best Practices**:

  - **Trust and Safety**: The Lighthouse report showed 7 insecure requests related to Cloudinary URLs.
  - **Reason**: Cloudinary hosts our media files, and during development, some images might be uploaded via HTTP. These requests are automatically upgraded to HTTPS by Cloudinary. However, Lighthouse still flags these as issues.
  - **Production Environment**: In our production environment, all media files are uploaded and served over HTTPS. Despite this, the warnings persisted in the Lighthouse report, affecting the best practices score.
  - **Resolution**: To address this, I ensured that all media uploads in both development and production environments are performed over HTTPS. Administrators should be aware of this when uploading media through the admin panel in the development environment.
  - **Impact**: These warnings do not affect the security of our application in production but are noted to explain the lower score in the best practices category.

  ### Known Bugs

- **Email Verification 500 Server Error**:
  - **Description**: During the registration process, users receive a confirmation email from our email provider, Mailjet. When users click on the verification URL in the email, they are redirected back to our application but encounter a 500 server error.
  - **Impact**: This issue prevents users from completing the email verification process, which is critical for activating their accounts.
  - **Workaround**: Registration through social apps (e.g., Google, Facebook) works as expected and does not encounter this issue.
  - **Current Status**: Unresolved. I'm investigating the root cause of the 500 server error and working towards a solution.
  - **Steps to Reproduce**:
    1. Register a new user account with an email address.
    2. Receive the email verification email from Mailjet.
    3. Click the verification URL in the email.
    4. Observe the 500 server error upon redirection back to the application.
  - **Additional Notes**: We have verified that the Mailjet configuration is correct and are currently debugging the application's email verification handler to resolve this issue.

**Budget Explorer** is designed to be a user-centric application that helps users find affordable places to visit while fostering a community where they can share their experiences and tips.

**Happy coding!**
