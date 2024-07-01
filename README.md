## Budget Explorer

"Budget Explorer" is a full-stack web application designed to help users find and share budget-friendly places to visit within a specified budget. The application allows users to input their budget, location, and number of people, and it returns a list of recommended places that fit their criteria. Users can also save their favorite places, view them on a map, and share their experiences.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Implementation Details](#implementation-details)
4. [User Stories and Agile Methodology](#user-stories-and-agile-methodology)
5. [Database Schema](#database-schema)

## Project Overview

Budget Explorer aims to help users discover affordable places based on their specific budget and location. Insp The application provides an interactive map, user reviews, and the ability to save favorite places. It is designed to be user-friendly and accessible, adhering to modern UX design principles.

This project was inspired by my wife’s experience during her first days after moving to Switzerland. She faced the challenge of browsing the internet to find budget-friendly places to visit. Budget Explorer aims to alleviate this struggle for anyone moving to a new country or simply looking to explore their surroundings on a budget. We hope it helps users connect with their new environment and find joy in discovering affordable adventures.

## Key Features

1. **User Authentication and Role-Based Access:**

- User registration and login via email(Mailjet https://app.mailjet.com/)
- Login using social platforms like Google and Facebook.
- Role-based access control (e.g., regular users vs. admin).

2. **Search and Filter:**

- Users can input their location, budget range, and number of people.
- The application provides a list of places that fit the user's criteria.
- Advanced filters like type of place, post title, or location.
- Users can filter posts to find them easily by title or location.
- The posts listing page updates to display only the posts that match the selected filters.
- "Near me" feature to filter places within a certain distance from the user's current location.

3. **Favorites:**

- Users can save their favorite places.

4. **Map Integration:**

- Interactive map displaying the locations of recommended places.
- Map view to explore places without leaving the site.
- User Experience (UX) and Accessibility:

5. **Intuitive and responsive design.**

- Clear feedback on user actions (e.g., adding to favorites, submitting reviews).

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
- Manual testing for both frontend and backend.
- Testing for functionality, usability, and responsiveness.

6. **Version Control:** Git, GitHub

7. **Deployment:**

Deploy on a cloud platform Heroku.

## User Stories and Agile Methodology

- Defined epics and broke them down into user stories and tasks.
- Track project progress, GitHub Projects: <a href="https://github.com/users/CedricNtwari/projects/3/views/1" target="_blank">Project Board</a>

## Database Schema

- **User:** Standard Django user model for authentication.
- **Place:** Stores information about each place (name, location, description, etc.).
- **Review:** Stores user reviews for places (comment, user, place).
- **Favorite:** Stores user's favorite places.

"Budget Explorer" is designed to be a user-centric application that not only helps users find affordable places to visit but also fosters a community where users can share their experiences and tips. By following the outlined features and implementation details using Django and TypeScript.

**Happy coding!**
