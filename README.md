## Budget Explorer

"Budget Explorer" is a full-stack web application designed to help users find and share budget-friendly places to visit within a specified budget. The application allows users to input their budget, location, and number of people, and it returns a list of recommended places that fit their criteria. Users can also save their favorite places, view them on a map, and share their experiences.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Implementation Details](#implementation-details)
4. [User Stories and Agile Methodology](#user-stories-and-agile-methodology)
5. [Database Schema](#database-schema)

## Project Overview

This project was inspired by my wife’s experience during her first days after moving to Switzerland. She faced the challenge of browsing the internet to find budget-friendly places to visit. Budget Explorer aims to alleviate this struggle for anyone moving to a new country or simply looking to explore their surroundings on a budget. We hope it helps users connect with their new environment and find joy in discovering affordable adventures.

## Key Features

1. **User Authentication and Role-Based Access:**

- User registration and login via email(Mailjet https://app.mailjet.com/)
- Login using social platforms like Google and Facebook.
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

- Users can save their favorite places.

![Favorites](/static/images/favorite.png)

4. **Map Integration:**

- Interactive map displaying the locations of recommended places.
- Map view to explore places without leaving the site.
- User Experience (UX) and Accessibility.

![Map Integration](/static/images/map.png)

5. **Intuitive and responsive design.**

- Clear feedback on user actions (e.g., adding to favorites, leave a comment, users can update their infos).

![Intuitive and responsive design](/static/images/Intuitive.png)
![users can update their infos](/static/images/user.png)

## Implementation Details

1. **Frontend:**

- HTML, CSS, Bootstrap for responsiveness and TypeScript for the responsive and interactive user interface.
- Use Django templates to render dynamic content.
  Consider using a front-end framework/library like .

2. **Backend:**

- Python with Django for handling backend logic, authentication, and database management.

3. **Database:**

- Relational database: PostgreSQL.
- Django ORM to define models for users, places, reviews, favorites, etc.

4. **Map Integration:**

- Use a mapping API like Google Maps to display locations.
- Integrate the map into Django templates.

5. **Testing:**

- Automated testing using Django's built-in testing framework.
- Manual testing for both frontend and backend, in different browser : Chrome, Firefox, Safari.
- Testing for functionality, usability, and responsiveness.

6. **Version Control:** Git, GitHub

7. **Deployment:**

Deploy on a cloud platform Heroku. https://budget-explorer-b9fdc935d3db.herokuapp.com/

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
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/#textarea)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
- Accessibility:
  - No errors were found when passing through web dev tool lighthouse
- JavaScript:
  - No errors were found when passing through the official [(Jshint) validator](https://jshint.com/)
- **Lighthouse**:

  - Tested with [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance, accessibility, best practices, and SEO.

  ![Lighthouse](/static/images/mobile.png)
  ![Lighthouse](/static/images/desktop.png)

### HTTPS Warnings Explanation

- **Best Practices**:

  - **Trust and Safety**: The Lighthouse report showed 7 insecure requests related to Cloudinary URLs.
  - **Reason**: Cloudinary hosts our media files, and during development, some images might be uploaded via HTTP. These requests are automatically upgraded to HTTPS by Cloudinary. However, Lighthouse still flags these as issues.
  - **Production Environment**: In our production environment, all media files are uploaded and served over HTTPS. Despite this, the warnings persisted in the Lighthouse report, affecting the best practices score.
  - **Resolution**: To address this, I ensured that all media uploads in the development and production environments are performed over HTTPS. As an admin should be aware of this when uploading media through the admin panel in the development environment.
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

"Budget Explorer" is designed to be a user-centric application that not only helps users find affordable places to visit but also fosters a community where users can share their experiences and tips. By following the outlined features and implementation details using Django and TypeScript.

**Happy coding!**

```

```
