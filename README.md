<h1  align="center">Culinary Connect</h1>

## Project Overview

**Culinary Connect** is a delightful platform for food enthusiasts to come together and share their passion for gastronomy. Our mission is to create a thriving community of culinary aficionados who can connect, collaborate, and celebrate the world of food.

Culinary Connect goes beyond the usual social media experience by focusing exclusively on the art of cooking, recipes, and the joy of savoring delicious dishes. Whether you're a professional chef, a home cook, or simply a food lover, you'll find a welcoming space to share your experiences and learn from others.

Join us in the Culinary Connect community to explore, connect, and create delicious moments together!

View the live project [here](https://culinary-connect-90809440f8f8.herokuapp.com//).

![Responsive Mockup](https://res.cloudinary.com/florindorneanu/image/upload/v1698666291/Screenshot_2023-10-30_at_12.44.13_huubq2.jpg)

## Table Of Contents
-   [User Experience Design (UX)](#user-experience-design-ux)
-   [The Strategy Plane](#the-strategy-plane)
-   [Project Objective](#project-objective)
-   [Agile Project Management](#agile-project-management)
-   [User Stories](#user-stories)
-   [The Structure Plane](#the-structure-plane)
-   [Project Structure](#project-structure)
-   [Features](#features)
-   [Future Features](#future-features)
-   [The Skeleton Plane](#the-skeleton-plane)
-   [Wireframes](#wireframes)
-   [Database Structure](#database-structure)
-   [The Surface Plane](#the-surface-plane)
-   [Design](#design)
-   [Technologies Used Frontend](#technologies-used-frontend)
-   [Technologies Used Backend](#technologies-used-backend)
-   [Testing](#testing)
-   [Deployment](#deployment)
-   [Credits](#credits)

## User Experience Design (UX)

## The Strategy Plane

### Project Objective

The central aim of the "Culinary Connect" project is to craft a compelling content sharing web application catering to the culinary community. This platform has been meticulously designed to facilitate users in the culinary world to:

- **Stay Informed:** Discover and stay updated on the latest happenings in the culinary domain.
- **Forge Connections:** Connect with fellow food enthusiasts and professionals to build a robust culinary network.
- **Engage with Culinary Content:** Interact with and contribute to the rich tapestry of culinary content shared on the platform.

Key features include:

- **Event Management:** Users can easily explore, create, edit, delete, culinary event listings, ensuring they never miss exciting food-related experiences.
- **Culinary Content Sharing:** Users can seamlessly view, create, edit, delete, like, and engage in discussions around culinary posts, creating a vibrant hub for culinary knowledge and inspiration.
- **Content Organization:** Culinary content is thoughtfully organized, offering options for enabling keyword and tag searches.
- **Profile Management:** Users can personalize their profiles, discover others in the culinary community, establish connections through following, and actively engage with shared culinary content.

This project is dedicated to delivering a unique platform that caters to the needs and passions of the culinary community, fostering continuous learning, networking, and active participation within the world of food and cooking.

### Agile Project Management

This project was meticulously managed through the application of agile methodologies, establishing an efficient workflow by implementing a Kanban board using GitHub Projects, which served as a pivotal project management tool. The Kanban board played a crucial role in visualizing our tasks, maintaining optimal work-in-progress limits, and enhancing overall workflow efficiency.

You can explore the Kanban board to gain insights into our project’s progression by following this [link](https://github.com/users/FlorinDorneanu/projects/5/5). 

Each user story was thoughtfully crafted with well-defined acceptance criteria. These stories were subsequently grouped into six distinct epics: Project Inception, API build, Frontend build, Testing, Documentation, and Deployment. The development process was anchored in a phased approach. It commenced by focusing on fulfilling the “must-have” requirements to ensure the delivery of core functionalities. Subsequently, the “should-have” features were addressed. This approach prioritized essential project prerequisites while allowing the integration of desirable features in an iterative, capacity-based manner.

![Image of Kanban](https://res.cloudinary.com/florindorneanu/image/upload/v1698662001/Screenshot_2023-10-30_at_11.01.13_foh86y.png)

![Image of Project Board](https://res.cloudinary.com/florindorneanu/image/upload/v1698662004/Screenshot_2023-10-30_at_11.00.56_qp9zaj.png)

### User Stories

#### Navigation & Authentication

- **US01. User Navigation:** 
    - As a culinary enthusiast, I want a user-friendly Navigation Bar available on all pages so that I can effortlessly navigate between different sections of the Culinary Connect application.

- **US02. Seamless Page Transitions:** 
    - As a food lover, I expect quick and seamless transitions between pages, allowing me to explore content without the need for page refreshing.

- **US03. Create an Account:** 
    - As a foodie eager to connect, I want to create a new account on Culinary Connect to access all the exciting features available to registered users.

- **US04. Sign-In:** 
    - As a culinary connoisseur, I'm eager to sign in to the app to unlock the full range of functionality available to logged-in users.

- **US05. User Authentication Status:** 
    - As someone passionate about culinary adventures, I want a clear indication of whether I'm currently logged in, ensuring I can quickly access my account when needed.

- **US06. Persistent Login:** 
    - As a user with a taste for culinary exploration, I expect my logged-in status to be maintained until I actively choose to log out, ensuring a seamless experience.

- **US07. Conditional Navigation Options:**
    - As a new culinary explorer, I look forward to seeing sign-in and sign-up options when logged out, making it easy to access these actions.

- **US08. User Avatars:** 
    - As someone who appreciates food as an art form, I want to view user avatars (profile pictures) to easily recognize and connect with other culinary enthusiasts within the application.

#### Posts

- **US09. Share Culinary Creations:** 
    - To showcase my culinary journey, I aim to create posts as a logged-in user, sharing my latest culinary creations with the community.

- **US10. Edit Culinary Posts:** 
    - As a culinary artist, I desire the ability to edit the post text, images, and tags of my creations, allowing me to refine and update my posts as needed.

- **US11. Remove Culinary Posts:** 
    - As the creator of delectable dishes, I should be able to delete my posts, ensuring they are no longer visible on Culinary Connect.

- **US12. Explore Culinary Posts:** 
    - To savor the diverse world of food, I want to be able to view the details of a culinary post, learning more about each unique creation.

- **US13. Browse Culinary Posts List:** 
    - As a culinary enthusiast, I look forward to seeing a list of culinary posts ordered by most recent, providing a delightful overview of the latest culinary inspirations.

- **US14. Search for Culinary Delights:** 
    - I anticipate being able to search for culinary posts using keywords and tags, helping me uncover mouthwatering recipes and profiles that match my culinary interests.

- **US15. Savor Posts from Followed Culinary Artists:** 
    - To stay updated with the culinary creations of fellow foodies, I aim to view posts from users I follow, savoring content tailored to my tastes.

#### Culinary Events

- **US16. Host Culinary Events:** 
    - As a culinary event organizer, I look forward to the ability to create and share culinary events with the Culinary Connect community.

- **US17. Event Updates:** 
    - As a culinary event host, I want the flexibility to edit event details, ensuring I can provide attendees with the latest updates and changes.

- **US18. Remove Events:** 
    - In my role as a culinary event organizer, I need the option to delete events, making them no longer visible to other Culinary Connect users.

- **US19. Explore All Culinary Events:** 
    - As a culinary event enthusiast, I eagerly anticipate viewing a comprehensive list of all culinary events, allowing me to plan my culinary adventures.

- **US20. Dive into Event Details:** 
    - For a deeper understanding of culinary events, I expect to access detailed information by viewing a single event page, getting all the culinary scoop.

- **US21. Search for Culinary Events:**
    - As a food lover with a taste for adventure, I want the ability to search for culinary events by titles, profiles, dates, or tags. This feature helps me discover culinary experiences that tantalize my taste buds.

- **US22. Event Updates from Followed Organizers:** 
    - To keep my culinary calendar full, I'm excited to view events from organizers I follow, ensuring I never miss a delectable event.

#### Culinary Like

- **US24. Savor Culinary Posts:** 
    - As a user with a passion for food, I can't wait to like culinary posts when logged in. This allows me to express my appreciation for mouthwatering creations.

- **US25. Update Likes:** 
    - As a culinary enthusiast, I appreciate the flexibility to unlike a post when logged in, should my culinary preferences change.

- **US26. Easily Find Liked Posts:** 
    - In my role as a user with a palate for great food, I expect to access the culinary posts I've liked, ensuring I can revisit my favorite culinary discoveries at any time.

#### Culinary Like Comment

- **US27. Savor Culinary Posts:** 
    - As a user with a passion for food, I can't wait to like comments from culinary posts when logged in.

- **US28. Update Likes:** 
    - As a culinary enthusiast, I appreciate the flexibility to unlike a comment when logged in, should my preferences change.


#### Culinary Comments

- **US30. Share Culinary Thoughts:** 
    - As a culinary enthusiast, I eagerly contribute culinary comments to posts when logged in, providing me with the opportunity to share my thoughts, recommendations, and culinary stories.

- **US31. Know Comment Timestamp:** 
    - In my role as a user with an appetite for knowledge, I value the ability to view the time elapsed since a culinary comment was made, helping me understand the latest culinary insights.

- **US32. Read Culinary Comments:** 
    - In the capacity of a culinary explorer, I look forward to reading culinary comments on posts, gaining insights into what other foodies think, recommend, and share about the dishes presented.

- **US33. Control Culinary Comment Removal:** 
    - As the owner of culinary comments, I expect to delete my own comments when logged in, giving me control over the culinary discussions and ensuring they remain relevant.

- **US34. Edit Culinary Comments:** 
    - While logged in and acting as a culinary comment owner, I want to edit my comments, empowering me to refine and update my culinary insights as needed.

#### Culinary Profiles

- **US40. Discover Culinary User Profiles:** 
    - As a culinary  explorer, I can't wait to explore the profiles of other foodies. This feature allows me to discover their culinary posts, events, and gain insights into their culinary journeys.

- **US41. Find Influential Culinary Profiles:** 
    - In my culinary journey, I have the opportunity to discover a list of the most influential culinary profiles. This functionality enables me to identify culinary enthusiasts who are widely followed and popular within the community.

- **US42. Manage Culinary Connections:** 
    - As a user on a culinary journey, I expect to follow or unfollow other culinary enthusiasts when logged in, giving me the power to curate my culinary feed by selecting the culinary voices I want to hear.

- **US43. Explore Culinary Posts from User Profiles:** 
    - In my culinary adventure, I anticipate the ability to access and review all culinary posts published by a specific user. This enables me to catch up on their recent culinary creations or decide whether to follow their culinary content.

- **US44. Discover Culinary Events from User Profiles:** 
    - As a food lover on a culinary exploration, I want to explore the culinary events listed by a specific user. This provides me with the opportunity to view their culinary events and decide whether I want to attend their culinary gatherings.

- **US45. Customize Culinary Profile Information:** 
    - In the culinary world, I expect to be able to edit my culinary profile, making changes to my profile picture and bio as needed. This functionality allows me to keep my culinary profile information up-to-date and relevant.

- **US46. Secure Culinary Profile Information:** 
    - In the culinary journey, I look forward to updating my username and password when logged in, ensuring that my culinary identity remains secure.

### Developer User Stories

**Profiles**

- **US47. Access All Culinary Profiles:**
    - As a developer/superuser, I have the capability to access a comprehensive list of all culinary profiles created, providing an overview of the diverse culinary community within Culinary Connect.

- **US48. Dive into Individual Culinary Profiles:**
    - In my role as a developer/superuser, I can delve into the details of an individual culinary profile to access specific user data, gaining insights into the culinary passions of our community members.

- **US49. Modify Personal Culinary Information:**
    - Being a developer/superuser, I have the authority to modify personal culinary information within a profile when logged in, ensuring users can keep their culinary details up-to-date.

- **US50. Remove User Accounts:**
    - In the capacity of a developer/superuser, I can perform user account deletions, ensuring the option to remove profiles from the API when necessary.

**Culinary Posts**

- **US51. List All Culinary Posts:**
    - As a developer/superuser, I can review a comprehensive list of all culinary posts in one view, facilitating efficient culinary post management.

- **US52. Access Culinary Post Details:**
    - In the role of a developer/superuser, I can view detailed information about a single culinary post, including any associated culinary comments, ensuring I have a full culinary picture.

- **US53. Create New Culinary Posts:**
    - Being a developer/superuser, I possess the capability to generate new culinary posts, ensuring their display within the culinary posts list for our community to enjoy.

- **US54. Edit Culinary Posts:** 
    - In my role as a developer/superuser, I can amend the content of culinary posts that I created, facilitating corrections or updates as necessary.

- **US55. Delete Culinary Posts:** 
    - In the capacity of a developer/superuser, I can remove culinary posts created by me, effectively eliminating culinary post data from the API.

**Culinary Events**

- **US56. List All Culinary Events:**
    - As a developer/superuser, I can access an extensive list of all culinary events at once, simplifying culinary event management within Culinary Connect.

- **US57. Access Culinary Event Details:**
    - In the role of a developer/superuser, I can view in-depth information about a single culinary event, including any associated reviews, ensuring I have a comprehensive understanding of our culinary gatherings.

- **US58. Create New Culinary Events:**
    - As a developer/superuser, I have the authority to generate new culinary events, ensuring their inclusion within the culinary events list, allowing our community to savor more culinary adventures.

- **US59. Edit Culinary Events:** 
    - As a developer/superuser, I can make modifications to culinary events I've created, allowing for updates and corrections to enhance the culinary event experience.

- **US60. Delete Culinary Events:** 
    - In the capacity of a developer/superuser, I can delete culinary events created by me, effectively removing culinary event data from the API to keep our culinary calendar up to date.

**Culinary Comments**

- **US61. Generate Culinary Comments:** 
    - As a developer/superuser, I can create culinary comments, associating them with specific posts, thus facilitating culinary user interaction and culinary discussion.
    
- **US62. View Culinary Comment List:** 
    - In my role as a developer/superuser, I can retrieve a complete list of all comments created within the API, making it easier to manage culinary discussions and interactions.

- **US63. Access Individual Comments by ID:** 
    - Being a developer/superuser, I can retrieve and view a single culinary comment using its unique identifier, making it possible to edit or remove comments when needed.

- **US64. Edit My Comments:** 
    - As a developer/superuser, I have the power to make edits to culinary comments I've created, allowing me to refine or update my culinary insights as necessary.

- **US65. Delete My Comments:** 
    - In the role of a developer/superuser, I can remove comments created by me, effectively eliminating comment data from the API, ensuring the discussions remain relevant.

**Culinary Liked**

- **US66. Create "Lived" Items:** 
    - As a developer/superuser, I can establish "liked" objects linked to culinary posts, allowing users to demonstrate their culinary appreciation.

- **US67. Delete "Loved" Items:** 
    - In my role as a developer/superuser, I can delete a "liked" object created by me, ensuring the ability to remove "liked" data from the API.

- **US68. Prevent Unauthorized Deletion:**
    - Being a developer/superuser, I can implement measures to prevent the unauthorized deletion of "liked" objects that I did not create.

- **US69. List All "Liked" Items:**
    - In my capacity as a developer/superuser, I can access a comprehensive list of all "liked" objects created in the API, facilitating the management of user interactions and culinary appreciation.


**Followers**

- **US70. Create a Follow:**
    As a developer/superuser, I can establish a "follow" relationship with another user, allowing users to connect and receive updates.

- **US71. View List of Follows:**
    In my role as a developer/superuser, I can access a list of all "follows" created within the API, providing insights into user connections.

- **US72. Delete Follow:**
    Being a developer/superuser, I can delete a "follow" relationship, offering users the option to unfollow another user's profile.

**Search and Filter**

- **US73. Implement Search Functionality:**
    As a developer/superuser, I can introduce a search field in both the events and posts lists, enhancing user experience by enabling search for specific events or posts.

- **US74. Filter Events by Category:**
    In my role as a developer/superuser, I can enable category-based event filtering, allowing users to view events related to a specific category.

- **US75. View Followed Profiles' Content:**
    Being a developer/superuser, I can provide a feature that allows users to see events and posts exclusively from profiles they follow.

- **US76. Display Liked Posts:**
    In my capacity as a developer/superuser, I can offer users a dedicated view of posts they've liked, simplifying post retrieval.

- **US77. Show Attending Events:**
    In the role of a developer/superuser, I can enable users to access a list of events they plan to attend, improving event tracking.

- **US78. Browse Content by User:**
    Being a developer/superuser, I can enable users to view events and posts created by a specific user, promoting personalized content discovery.

- **US79. Retrieve Post Comments:**
    In my capacity as a developer/superuser, I can provide a feature that allows users to access comments linked to a particular post, enhancing the understanding of user interactions.

**Culinary Liked Comments**

- **US80. Create "Liked" Comments:** 
    - As a developer/superuser, I can establish "liked" objects linked to comments from culinary posts, allowing users to demonstrate their appreciation.

- **US81. Delete "Loved" Items:** 
    - In my role as a developer/superuser, I can delete a "liked comment" object created by me, ensuring the ability to remove "liked comment" data from the API.

- **US82. Prevent Unauthorized Deletion:**
    - Being a developer/superuser, I can implement measures to prevent the unauthorized deletion of "liked comment" objects that I did not create.

- **US83. List All "Liked" Items:**
    - In my capacity as a developer/superuser, I can access a comprehensive list of all "liked comments" objects created in the API, facilitating the management of user interactions and culinary appreciation.


## The Structure Plane

### Project Structure

Culinary Connect exhibits two distinct user experiences contingent upon the user's authentication status. Whether logged in or logged out, these states dictate varying content accessibility and user capabilities.

For logged-out users, the Navigation Bar provides access to the Home, About, Sign In, and Sign Up pages. Upon logging in, the user gains access to additional features within the Feed, encompassing Posts, Events, Liked, Sign Out, and the Profile Page.

The transition to a logged-in state empowers users with the ability to perform actions beyond the scope of logged-out users:
Logged-in users can create events and posts, modify their profile details, including their username and password, manage their comments, express their preference for posts through likes and unlikes, express their preference for comments through likes and unlikes and expand their network by following or unfollowing other users.

## Features

### Navigation

The navigation bar boasts an elegant and minimalist design, ensuring an exceptional user experience. Its appearance dynamically adapts based on your authentication status. On tablets and mobile devices, the navigation bar transforms into a user-friendly hamburger menu.

When a user is logged out, the following menu items are readily accessible:

- **Culinary Connect Logo:** This logo serves as a constant presence across the site, providing all users with a convenient link back to the homepage.
- **Home:** Users can navigate to the "Home" section, where a diverse array of posts populates the platform.
- **Authentication:** For quick access, the "Sign In" and "Sign Up" icons are prominently displayed, offering seamless entry into the respective authentication processes.

- **Feed:** Logged-in users can explore content from profiles they follow.

- **Authentication:** The authentication icons transform as well. Instead of displaying "Sign In" and "Sign Up" options, they now feature a direct link to the user's profile page and a convenient "Sign Out" option to exit the site.

- **Add Event and Add Post:** For users who are logged in, links to create new events and posts are readily accessible.

### Authentication

Users who have not created an account can click on the Sign Up link on the Navigation Bar to create a user account. I have used the standard dj-rest/auth/registration user account signup process for this.

If a user has a Culinary Connect user account, they can click on the Sign In menu option in the Navigation Bar to sign into their account.

To sign out, already signed in users can access the Sign Out option in the Navigation Bar.

### Posts Page / Homepage

The Posts Page, which also serves as the website Homepage, consists of three main React components:

1. **Popular Profiles Component**
2. **Posts**
3. **Search**

- **Popular Profiles Component**

The Popular Profiles Component is a prominent feature throughout the website. On larger screens, it appears to the right of all pages, while on smaller screens, it occupies the top section. This component utilizes a filter to rank all site users by their follower count, listing the top ten profiles on larger screens and the top four on smaller screens.

For users who aren't logged in, the component displays the profile avatar and the username. In contrast, logged-in users have the additional option to follow or unfollow the profile. Clicking on any profile avatar allows the user to view the complete profile page of that individual.

- **Posts**

The Posts section showcases all posts created by users on the platform. Posts are retrieved from the API, sorted by creation date, with the most recent posts featured at the top in descending order.

Each post includes details about the user who created it, the date of creation, the title, the written description, an image, location and relevant tags. Users can also view the number of likes and comments on each post. Clicking on the post image or the comments count takes the user to the post's individual page.

- **Search**

To find specific posts, users can utilize the search bar. This feature enables searching by the username of the post creator, the written content within the post, and associated post tags.

### Events Page

The Events Page shares a similar layout with the Posts Page and utilizes several key components. The Events Page is made up of the following main React components:

1. **Popular Profiles Component**
2. **Event**
3. **Search and Filter**

- **Event**: 
  The Events Page displays all events created by users on the Culinary Connect platform. These events are retrieved from the API and sorted by creation date, with the most recently created events appearing at the top in descending order.

  Each event provides information about the user who created it, the creation date, the event title, description, date, category, image, and tags. Clicking on the event image directs users to the event's dedicated page.

- **Search**:
  Users can easily search for specific events using the search bar. They can search for events based on the username of the creator, the event description, and event tags.

### Feed

To access the feed page, simply click on the 'Feed' option in the Navigation Bar. The Posts Feed and Events Feed pages have a familiar layout reminiscent of their respective Posts Page and Events Page counterparts. However, their function diverges in how content is filtered. On the feed pages, they pull all Posts and Events from the API, but the magic happens with the applied filter. This filter ensures that only Posts or Events created by profiles that the logged-in user follows are displayed. Keep in mind that this page is exclusively accessible to logged-in users. In cases where a user isn't following any profiles yet, a 'No Results Found' message will be thoughtfully presented.

### Create a Post

Logged-in users have the privilege to share their thoughts and experiences with the community by creating new posts. By selecting the 'Add Post' option from the Navigation Bar, users are seamlessly directed to the Create Post form. This user-friendly form demands all essential fields to be filled, and it's worth noting that uploading an image is mandatory for successful submission. After submitting the form, the newly created post is swiftly available on the Posts Page. Users will be automatically redirected to the post's individual page, where they can view their masterpiece. Additionally, for every post created, the user's posts count increases, proudly displayed in their profile page stats for others to see their engagement and contribution.

### Create an Event

For users who are logged in, the opportunity to host and share exciting events with the community is just a click away. By selecting the 'Add Event' option from the Navigation Bar, users are guided to the Create Event form. Every field in this form is required, and the inclusion of an image is crucial for a successful event submission. Once the form is submitted, users can immediately access the newly created event on the Events Page. A swift redirection takes users to the event's dedicated page, allowing them to view and share it. Furthermore, each event hosted increases the user's events count, which is prominently showcased in their profile page stats, offering insight into their contributions as event hosts.

### Post Page

The Post Page offers a detailed view of an individual post, presenting both post details and comments. Users can access this page by clicking on the post image or comment icon from the Posts Page or Posts Feed. If the user is the post's owner, they gain the ability to edit or delete the post by selecting the three dots next to the post's creation date.

Beneath the post details lies the comments section. In the absence of comments, users encounter a message indicating no comments have been posted. When users are not logged in, they can read published comments but cannot create comments until they log in. Once logged in, a comment form appears above existing comments, allowing users to share their thoughts on the post.

Choosing the "Delete" option removes the post from the API, making it invisible on the platform. Users are then redirected to the Post Create form, offering the option to create a new post. Opting for "Edit" redirects users to the Post Edit Form, pre-populated with the existing post's information. Users can modify this information, save the changes, and return to the Post Page, now featuring the updated post.

### Event Page

The Event Page provides a comprehensive display of a specific event's details. Users can navigate to this page by clicking on an event image from the Events Page or Events Feed. If the user is the event's organizer, they have the option to edit or delete the event by selecting the three dots next to the event's creation date.

Opting for "Delete" removes the event from the API, rendering it invisible on the platform. Users are then redirected to the Event Create form, providing the opportunity to create a new event. If "Edit" is selected, users are directed to the Event Edit Form, pre-filled with the existing event's information. Users can make adjustments, save the changes, and view the updated event on the Event Page.

### Comments

On each Post Page, a "Post a Comment" button invites users to engage with that specific post. The comment form includes a single text input field for users to compose their comments. All fields are required, ensuring that comments are not published unless text is provided. Upon publishing a comment, the comment count visibly increments for that post.

Comment owners who wish to make modifications to their comments after publishing have the option to edit or delete comments by using the three dots menu located to the right of the published comment.

### Profile Page

The Profile Page provides an in-depth look at a user's identity and activity on Culinary Connect. Users can access Profile Pages by clicking on profile avatars found throughout the site, including popular profiles, post and event authors, and comments. Users can also access their own Profile Page via the authentication icon in the Navigation Bar.

A user's Profile Page displays various information, including:

- Profile picture
- Username
- Profile Stats
- About section
- Published posts
- Published events

When a user signs up for Culinary Connect, a basic profile is automatically created with a username, password, and default avatar image. The only information initially generated on the profile page is the user's Profile Stats, which encompass:

- The number of events the user has published
- The number of posts the user has published
- The number of profiles the user is following
- The number of profiles following the user

The user's "About" section remains blank until the user visits their own Profile Page and chooses to edit the profile by adding personal details. Clicking on the "Edit Profile" option leads them to a form where they can update their profile picture and about section. Users have the flexibility to share as much or as little personal information as they prefer.

Each profile also includes a "Follow" button, allowing other users to follow or unfollow that profile. The user's published posts and events are listed on their Profile Page, which can be accessed through React-Bootstrap tabs for easy navigation.

### Reusable React Components

1. **Asset**
    - This versatile component is used throughout the website to load images, display messages, and indicate loading spinners.

2. **Avatar**
    - The Avatar component is consistently utilized to display user avatars across different pages of the website.

3. **NavBar**
    - The NavBar component serves as the primary navigation bar and is consistently present on every page of the website.

4. **Not Found**
    - The Not Found component is presented to users when they attempt to access an invalid URL.

5. **MoreDropdown**
    - Reused to enable users to edit and delete various items, such as events, posts and comments.

### Future Features

1. **Real-time User Interactions**
 - Enjoy real-time chat, notifications, and user-to-user messaging for seamless communication.
2. **Personalised User Profiles**
- Customise your profile further, adding new sections and options to make it uniquely yours.
3. **Mobile App Development**
- Stay tuned for the mobile app, extending accessibility to your favorite environmental platform.

## The Skeleton Plane

### Wireframes

<details><summary>Logged In User Home Page</summary>


![Logged in](https://res.cloudinary.com/florindorneanu/image/upload/v1698664669/Logged_in_homepage_vyazew.png)

  

</details>


<details><summary>Logged Out User Home Page</summary>

  

![Logged Out](https://res.cloudinary.com/florindorneanu/image/upload/v1698664747/Logged_Out_homepage_nebgkl.png)

### Database Structure

I've crafted the database structure for the Culinary Connect Backend API. Here are the core models:

- **Users:** These are slightly customized from Django's standard User model to align with our requirements.
- **Profiles:** Automatically generated upon user registration, these profiles are tailored to encompass essential information.
- **Posts:** Users can create posts, which are shared on the platform.
- **Likes:** Indicate if a user appreciates another user's post.
- **Comments:** Enable users to provide feedback and commentary on posts.
- **Events:** Users can create posts for upcoming events, providing valuable event details.
- **Likecomment:** Indicate if a user appreciates another user's comment.
- **Followers:** Empower users to follow each other within the platform.

To understand the relationships between these models, please refer to the Entity-Relationship diagram:

![Entity Relationship Diagram]()

A few considerations about the ER diagram:

- The diagram represents a logical data model, emphasizing the relationships between entities.
- The Users table in the diagram offers a logical view of user registration data and its connection to the application's data model. Please note that it doesn't encompass all the columns and constraints within the physical database tables managed by Django modules.


# Culinary Connect

## Design

### Colour Scheme

The "Culinary Connect" project embraces a distinct color scheme that mirrors its unique identity and culinary mission. These carefully chosen colors draw inspiration from the world of food, emphasizing the platform's commitment to culinary exploration.

- **Slate Blue (#4682B4)**: This rich hue reflects the depth and richness of the culinary world, symbolizing the diverse flavors and experiences within it.

- **Light Steel Blue (#B0C4DE)**: Light steel blue represents the freshness and creativity found in the culinary arts, highlighting our dedication to innovative cooking.

- **Tomato Red (#FF4136)**: The vibrant tomato red showcases the passion and energy that cooking enthusiasts bring to Culinary Connect, symbolizing the love for food.

- **Whisper Gray (#F1F5F7)**: Whisper gray, a subtle and inviting tone, signifies community and sharing, embodying the sense of togetherness that Culinary Connect encourages.

This thoughtfully curated color palette resonates with users who share our enthusiasm for culinary exploration. It serves as a visual reminder of our mission to connect food lovers and create a delightful culinary world. The exact hex colors and color scheme were generated by the [https://coolors.co/](https://coolors.co/) color scheme generator.

#### Typography

In the "Culinary Connect" project, the Playfair and Kanit fonts have been thoughtfully chosen to elevate the visual aesthetics and legibility of the platform. These fonts contribute to a unique typographic experience, enhancing the overall design and readability of the content.

**Playfair** is an elegant and timeless serif font that brings a touch of sophistication to Culinary Connect. Its graceful letterforms and high contrast design make it ideal for headlines and creative text elements. You can find Playfair on [Google Fonts](https://fonts.google.com/specimen/Playfair+Display).

**Kanit** is a contemporary and highly legible sans-serif font that ensures readability and accessibility. It offers a clean and modern aesthetic, making it suitable for body text and user interface elements. Kanit can be sourced from [Google Fonts](https://fonts.google.com/specimen/Kanit).

This combination of Playfair and Kanit strikes a harmonious balance between style and functionality, complementing Culinary Connect's overall design. These fonts enhance the visual appeal, accessibility, and readability of the platform, providing users with a delightful and engaging experience. The Playfair and Kanit fonts contribute to a more elegant and easily readable environment, making Culinary Connect a truly enjoyable destination for all food enthusiasts.

#### Logo
    
The logo was created with the [logo.com](https://logo.com/)  logo generator. I selected the typography, colour scheme, and icon, and then applied it through the website and as the favicon. Legibility was a priority, as well as its clear portrayal of the app purpose.

#### Imagery

- The images for the posts, events and profiles created on the website were sourced from free stock image provider [Pexels](https://www.pexels.com/)
- The icons were imported from [Font Awesome](https://fontawesome.com/).

## Testing

Please click [here](TESTING.md) to read more information about testing Culinary Connect's frontend and backend.

## Technologies Used Frontend

### Languages

-   [HTML5](https://en.wikipedia.org/wiki/HTML)  - Provides the content and structure for the website
-   [CSS3](https://en.wikipedia.org/wiki/CSS)  - Provides the styling for the website
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)  - Provides interactive elements of the website
-   [React.js](https://en.wikipedia.org/wiki/React_(software))  - Provides the base for the frontend components

### Frameworks, Software and Web Applications

-   [React Bootstrap](https://react-bootstrap.github.io/)  - A CSS framework that helps build solid, responsive, mobile-first sites
-   [Balsamiq](https://balsamiq.com/)  - Used to create the wireframes
- [Coolors](https://coolors.co/)  - Used to pick the colour scheme of the website 
-   [Github](https://github.com/)  - Used to host the repository, store the commit history and manage the project board containing user stories
-   [Heroku](https://en.wikipedia.org/wiki/Heroku)  - A cloud platform that the application is deployed to
-   [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)  - Used to test site performance
- [Logo](https://logo.com/)  - Used to generate the logo
-   [Favicon](https://favicon.io/)  - Used to create the favicon
-   [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)  - Used to debug and test responsiveness
- [Google Fonts](https://fonts.google.com/specimen/DM+Sans) - Used to import the website font 
-   [Cloudinary](https://cloudinary.com/)  - A service that hosts image files in the project.
-   [HTML Validation](https://validator.w3.org/)  - Used to validate HTML code
-   [CSS Validation](https://jigsaw.w3.org/css-validator/)  - Used to validate CSS code
-   [JSHint Validation](https://jshint.com/)  - Used to validate JavaScript code
- [Pexels](https://www.pexels.com/) - Free stock image provider for posts, events and avatars that were uploaded 
- [Font Awesome](https://fontawesome.com/) - Used for icons across UI

## Technologies Used Backend

### Languages

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>) - Provides the functionality for the DRF backend framework.

### Frameworks & Software

- [Django Rest Framework](https://www.django-rest-framework.org/) - A framework for building web API's
- [PEP8 Validation](https://pypi.org/project/pep8/) - pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
- [Github](https://github.com/) - Used to host the repository, store the commit history and manage the project board containing user stories.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
- [Cloudinary](https://cloudinary.com/) - A service that hosts image files in the project.

### Libraries

The libraries used in this project are located in the requirements.txt file and have been documented below

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
- [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary.
- [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - Drop-in API endpoints for handling authentication securely in Django Rest Framework.
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
- [django-filter](https://pypi.org/project/django-filter/) - Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.
- [django-taggit](https://pypi.org/project/django-taggit/) - Django-taggit a simpler approach to tagging with Django.
- [django-rest-framework](https://pypi.org/project/djangorestframework/) - web-browsable Web APIs.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
- [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [pillow](https://pypi.org/project/Pillow/8.2.0/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
- [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
- [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
- [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - P rovides first-class OAuth library support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python.

## Deployment Frontend

### Deployment to Heroku

Once you have created a new gitpod workspace and set up the new project, you are ready to deploy to Heroku.

1.  In your heroku account, select Create New App, and give it a unique name related to your project.
2.  Select a region corresponding to where you live and click 'Create App'.
3.  Head into the 'Deploy' tab select GitHub as the 'deployment method', find your project repository and click 'Connect'.
4.  Click 'Deploy branch' to trigger Heroku to start building the application.
5.  Once you see the message saying 'build succeeded' you can click 'Open App' to see your application in the browser.

### Fork this Project Repository

It is possible to make an independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to make changes in the copy without affecting the original repository. To fork the repository, follow these steps:

1.  After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

### Clone this Project Repository

A Git clone creates a linked copy of the project that will continue to synchronize with the original repository. In order to create a clone, you can click on the 'Code' button inside the selected repository and then select the 'Clone' option from the dropdown list.

## Deployment Backend

The project was deployed to [Heroku](https://www.heroku.com/). To deploy, please follow the process below:

1.  To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.
2.  Fill in the details for the new repository and then click 'Create Repository From Template'.
3.  When the repository has been created, click on the 'Gitpod' button to open it in the GitPod Editor.
4.  Now it's time to install Django and the supporting libraries that are needed, using the following commands:

- `pip3 install 'django<4' gunicorn`
- `pip3 install 'dj_database_url psycopg2`
- `pip3 install 'dj3-cloudinary-storage`

5.  When Django and the libraries are installed we need to create a requirements file.

- `pip3 freeze --local > requirements.txt` - This will create and add required libraries to requirements.txt

6.  Now it's time to create the project.

- `django-admin startproject YOUR_PROJECT_NAME .` - This will create the new project.

7.  When the project is created we can now create the applications. My project consists of the following apps; Profiles, Comments, Contact, Events, Followers, Going, Interested and Reviews.

- `python3 manage.py startapp APP_NAME` - This will create an application

8.  We now need to add the applications to settings.py in the INSTALLED_APPS list.
9.  Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

- `python3 manage.py makemigrations` - This will prepare the migrations
- `python3 manage.py migrate` - This will migrate the changes
- `python3 manage.py runserver` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

9.  Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

- Once signed into your [Heroku](https://www.heroku.com/) account, click on the button labeled 'New' to create a new app.

10. Choose a unique app name, choose your region and click 'Create app".

11. Next we need to connect an external PostgreSQL database to the app from [ElephantSQL](https://customer.elephantsql.com/login). Once logged into your ElephantSQL dashboard, you click 'Create New Instance' to create a new database. Give the database a:

- Name
- Tiny Turtle Free Plan
- Selected data center near you

and click 'Create Instance'. Return to your ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.

12. Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the app.

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

- `import os` - This imports the os library
- `os.environ["DATABASE_URL"]` - This sets the environment variables.
- `os.environ["SECRET_KEY"]` - Here you can choose whatever secret key you want.

14. Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore file so that it isn't commited to GitHub for other users to find.

15. Now we have to connect to our environment and settings.py file. In the settings.py, add the following code:

`import os`

`import dj_database_url`

`if os.path.isfile("env.py"):`

`import env`

16. In the settings file, remove the insecure secret key and replace it with: `SECRET_KEY = os.environ.get('SECRET_KEY')`

17. Now we need to comment out the old database settings in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

Instead, we add the link to the DATABASE_URL that we added to the environment file earlier.

18. Save all your fields and migrate the changes again.

`python3 manage.py migrate`

19. Now we can set up [Cloudinary](https://cloudinary.com/users/login?RelayState=%2Fconsole%2Fmedia_library%2Ffolders%2Fhome%3Fconsole_customer_external_id%3Dc-95a4cb26371c4a6bc47e19b0f130a1#gsc.tab=0) (where we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

`os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`

21. Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

22. Back in the settings.py file, we now need to add our Cloudinary Libraries we installed earlier to the INSTALLED_APPS list. Here it is important to get the order correct.

- cloudinary_storage
- django.contrib.staticfiles
- cloudinary

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

24. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to the ALLOWED_HOSTS list:

`ALLOWED_HOSTS = ['name.herokuapp.com', 'localhost']`

25. Now we just need to create the basic file directory in Gitpod.

- Create a file called \*_Procfile_ and add the line `web: gunicorn PROJ_NAME.wsgi?` to it.

26. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

- `git add .`
- `git commit -m "Deployment Commit`
- `git push`

27. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

28. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

### How To Fork The Repository On GitHub

It is possible to make an independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to make changes in the copy without affecting the original repository. To fork the repository, follow these steps:

1.  After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

### Cloning And Setting Up This Project

To clone and set up this project you need to follow the steps below.

1.  When you are in the repository, find the code tab and click it.
2.  To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3.  Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4.  Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.
5.  To be able to get the project to work you need to install the requirements. This can be done by using the command below:

- `pip3 install -r requirements.txt` - This command downloads and installs all required dependencies that is stated in the requirements file.

6.  The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

- `python3 manage.py migrate` - This will do the necessary migrations.
- `python3 manage.py runserver` - If everything i setup correctly the project is now live locally.

## Credits

-   [React Bootstrap documentation:](https://react-bootstrap.netlify.app/)  - Documentation used for styling and to build responsive web pages
-   [Code Institute:](https://codeinstitute.net/)  Walkthrough modules for the Moments app
-   [Code Institute Slack Community:](https://app.slack.com/)  Slack community for troubleshooting and FAQ.
-   [Code Institute Tutor Support:](https://app.slack.com/)  For help and support
-   [React documentation:](https://legacy.reactjs.org/docs/getting-started.html)  Everything you need to know about React
-   [Stack Overflow:](https://stackoverflow.com/)  For troubleshooting and FAQ
-   [W3Schools:](https://www.w3schools.com/)  Online Web Tutorials
-   [Django Taggit documentation](https://django-taggit.readthedocs.io/en/latest/api.html) 

