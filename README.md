README

# LuGa|Talk

Welcome to Luga|Talk, where the vibrant beats of Luga-flow meet the rich tapestry of Luganda, also known as Ganda, spoken by millions in Uganda.

Luga|Talk is more than just a blog; it's a celebration of culture, language,and connection. Just as Luga-flow infuses contemporary hip-hop with traditional Ugandan rhythms, our platform intends to also blend the beauty of Luganda with modern storytelling.

Discover the rhythm and melody of Luganda as you immerse yourself in our community. Whether you're here to learn, connect, or simply explore, Luga|Talk invites you to experience the warmthof Ugandan hospitality and embark on a journey of cultural understanding.

Join us as we delve deeper into the heart of Luganda and embrace the spirit of Luga-flow. Let's journey together towards mastering this incredible language and embracing the diversity it embodies.

![Mockup image](/docs/mockup.png)
<br>
Developer: Edgar Kimbugwe <br>
[Live webpage](https://lugatalk-ab90580d7f17.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Database](#database)
    1. [Luga App](#luga-app)
    2. [User App](#user-app)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)

## Project Goals

At Luga|Talk, we aim to celebrate and promote the Luganda language and Ugandan culture through engaging content and a vibrant community. Our goals reflect the aspirations of our project, our users, and the site owners, ensuring a comprehensive and enriching experience for everyone involved.

- Increase awareness and appreciation of Luganda globally by providing resources for learning and improving the language skills.
- Highlight Buganda's cultural practices and traditions through shared stories, music, and other expressions unique to Buganda.
- Create a space where Luganda speakers and learners can connect by interacting through the wesite's comments and replies section.
- Inspire Modern Storytelling by showcasing modern narratives and voices within the context of Luganda and Ugandan culture.
- Share educational resources and tools related to the Luganda language, Buganda and Ugandan culture as a whole. 

### User Goals
- Find comprehensive and accessible resources for learning Luganda
- Explore and understand Buganda culture and traditions by engaging with stories, music, and content reflecting the essence of Buganda.
- To interact with other Luganda learners and native speakers by participating in discussions, forums, and community events.
- Accessing their personal blog-posts, which will entail their added blog posts and favourite blog posts posted by other users. 
- Utilize articles, tutorials, videos, and other educational materials.

### Site Owner Goals
- Providing a platform for audience interested in learning Luganda and exploring Buganda or Ugandan culture
- Offering users the ability to Create and manage their own blog posts.
- To ensure all content added is well-researched, accurate, and engaging
- Encourage active participation from users through comments, forums, and social media
- Explore and implement monetization strategies to generate revenue for operations and growth of the site

[Back up](#table-of-content)

## User Experience

### Target Audience
At Luga|Talk we will aim to the following target audience:

- Individuals interested in learning Luganda, from beginners to advanced learners.
- Ugandans living abroad who want to stay connected with their culture and language.
- People fascinated by Buganda culture, music, and traditions who seek to explore and understand more.
- Linguists and language enthusiasts looking to expand their knowledge of lesser-known languages.

### User Requirements and Expectations
When using the Luga|Talk blog platform, users can expect the following features and characteristics to meet their requirements:

- Users expect tutorials, articles, and multimedia content to aid in understanding and learning about the Luganda language.
- High-quality, diverse content that is both informative and entertaining, including stories, music, and cultural insights.
- Responsive design that is intuitive, easy to navigate, and responsive across all devices.
- Personalized feature to store favorite blogs, track personal blog posts additions, and add comments to blog posts.
- Access to a diverse collection of material in regard to Luganda as a language and the cultural and tradition of Buganda / Uganda.

Luga|Talk aims to create an engaging platform for users to explore, discover, and share their love for learning and writing on a topic of their interest, the Luganda languange.

### User Stories

#### Epic 1: User Authentication and Account Management

- [As a User I can create an account so that I can interact with blog posts.](https://github.com/Edgarkimbugwe/django-blog/issues/17)<br>
- [As a Registered User, I can view my profile, so that I can manage my information.](https://github.com/Edgarkimbugwe/django-blog/issues/18)<br>
- [As a Site Admin I can view and manage user accounts so that I can ensure the security of the site and the users.](https://github.com/Edgarkimbugwe/django-blog/issues/14)<br>
- [As a Site User I can create an account so that I can interact with blog posts.](https://github.com/Edgarkimbugwe/django-blog/issues/17)<br>

#### Epic 2: Blog post Management
- [As a Registered user I can edit my own blog posts so that I can update them when need be.](https://github.com/Edgarkimbugwe/django-blog/issues/16)<br>
- [As a Site User, I can view a paginated list of posts so that I can browse through the content easily without being overwhelmed by too many posts at once](https://github.com/Edgarkimbugwe/django-blog/issues/33)<br>
- [As a Registered User, I can create a blog post, so that I can share my thoughts and engage with the community.](https://github.com/Edgarkimbugwe/django-blog/issues/19)<br>
- [As a Registered User, I can like blog posts, so that they are added to my favourite posts.](https://github.com/Edgarkimbugwe/django-blog/issues/24)<br>
- [As a Registered User, I can comment on blog posts, so that I can share my thoughts and engage with the community.](https://github.com/Edgarkimbugwe/django-blog/issues/18)<br>
- [As a Registered User, I can delete my blog post, so that I can remove a post if i want to.](https://github.com/Edgarkimbugwe/django-blog/issues/20)<br>
- [As a Site Admin, I can create draft blog posts so that I can complete the content at a later time.](https://github.com/Edgarkimbugwe/django-blog/issues/31)<br>
- [As a Site Admin, I can approve or reject comments, so that the quality of discussions on the blog are effective.](https://github.com/Edgarkimbugwe/django-blog/issues/23)<br>

#### Epic 3: User Experience and Site Information
- [As a Site User I can see the about page of the blog so that have an insight of blogs posted](https://github.com/Edgarkimbugwe/django-blog/issues/32)<br>
- [As a Site User, I can browse the blog posts so that I can read articles of interest](https://github.com/Edgarkimbugwe/django-blog/issues/15)<br>

[Back up](#table-of-content)

## Database
Luga|Talk uses the following database scheme:
<details><summary>See Database Scheme</summary>
<img src="docs/database.png">
</details>

### Luga App
This is the core component of the LugaTalk project, responsible for managing blog posts, comments, and user interactions with the content.
- Blog Post Management: Facilitates the creation, publication, and management of blog posts. This is, create, edit and delete a post. 
- Commenting System: Allows users to add comments to blog posts and ensures that comments require approval before being displayed
- User Engagement and Interaction: Enhances user engagement by allowing them to express appreciation for content by liking a post. 
- Personalized Content: To provide a personalized content experience, posts authored and liked by the logged-in user are displayed to the registered users account. 

### User App
The 'User App' handles user management, including registration, profile management, and authentication.
- User Registration and Authentication: Allows new users to register and existing users to log in and out of the system securely.
- Profile Management: Enables users to manage and update their profile information, including personal details and adding a profile pictures stored through cloud-based hosting.
- User Account and Data Handling: Ensures that user-related data is properly managed, including account deletion and related data cleanup.

[Back up](#table-of-content)

## Design
The design of the LugaTalk website is user-centric, blending modern aesthetics with intuitive navigation. It features a clean, responsive layout optimized for readability and user engagement. The design elements highlight the cultural richness of Luganda while ensuring a seamless user experience across devices.

By embracing a minimalistic design, LugaTalk ensures that the focus remains on the rich cultural content and stories shared within the community. The use of ample white space, intuitive navigation, and clear typography enhances readability, allowing the beauty of language and vibrant blog content to take center stage."

### Design Choices
The website features a minimalistic, responsive design that emphasizes readability and cultural aesthetics. The color palette, including shades like subtle pastels, enhances visual appeal and reflects the vibrancy of Luganda culture. Clear typography and intuitive navigation improve the user experience, while interactive elements like comments and likes foster community engagement

### Colour
The color palette is thoughtfully chosen to reflect the cultural richness and vibrancy of Luganda while maintaining a clean, minimalistic aesthetic. The use of subtle, harmonious colors creates a warm and inviting atmosphere without overwhelming the user. This approach enhances readability and ensures that the focus remains on the content. By avoiding background images, the design prioritizes simplicity and speed, providing a distraction-free experience that highlights the textual and visual content of the blog posts.

![Mockup image](/docs/colorpalette.png)

### Fonts
The project utilizes the default fonts provided by Bootstrap 5, ensuring a clean and professional look that enhances the overall user experience. However, users have the flexibility to customize and style fonts during content creation and editing to add their unique touch.

### Structure
The Luga|Talk features a user-friendly and intuitive design, ensuring easy navigation and comprehension for users. It is structured into distinct sections and pages as follows:

#### Before Logged In:

- **Landing Page** Here, visitors are immediately greeted with the latest posts, reflecting the design's focus on showcasing recent content first.<br>
- **About Page:** The "About" page provides an introduction to LuGa|Talk, highlighting its celebration of Luga-flow and Luganda culture, language, and community engagement.<br>
- **Register Page:** The register page allows new users to create accounts, providing access to personalized features and community engagement.<br>
- **Login Page:** The login page enables registered users to securely access their accounts and interact with the platform's content and community.<br>

#### When Logged In:
Upon logging in, users are still directed to the most recent posts however unlike unregistered users, they can access extra functionalities through additional links which are revealed, providing access to specific profile-related pages and actions. 

- **New Post:** The "New post" page enables users to Add posts by providing a user-friendly form to input content for the blog post they want to create and have an option to apply own fonts when creating posts. .<br>
- **My Blog posts page:** This page allows users to view and manage their created blog post allowing them to either edit or delete them. Also this page list the users favorite posts that they have liked.<br>
- **Commenting:** Logged-in users have the ability to engage with blog posts by leaving comments and participating in discussions.<br>
- **Profile Page:** The profile page displays the user's profile information, including their bio, profile picture, and other relevant details. It allows users to update and customize their profile settings. At the top of this page, the link to the user's blog posts is available, so that the user gets access to their blog posts and liked posts under 'my favorite posts'.<br>
- **Logout:** The "Logout" option allows users to securely log out of their accounts, ensuring the privacy and security of their personal information.<br>

Luga|Talk's structured design ensures a seamless and enjoyable user experience, allowing users to effortlessly explore, contribute to, and manage their blog posts.

### Wireframes
The wireframes visually depict various pages and features of the web application, serving as blueprints for designing each page. They provide a clear visualization of the user interface and overall user experience, created efficiently with Balsamiq—a tool designed for quick and intuitive sketching of design concepts.

<details><summary>Home Page (landing page)</summary>
<img src="docs/wireframes/index.png">
</details>
<details><summary>About</summary>
<img src="docs/wireframes/about.png">
</details>
<details><summary>Register</summary>
<img src="docs/wireframes/register.png">
</details>
<details><summary>My Blog Postss</summary>
<img src="docs/wireframes/myblogs.png">
</details>
<details><summary>New Post</summary>
<img src="docs/wireframes/createblog.png">
</details>
<details><summary>Login</summary>
<img src="docs/wireframes/login.png">
</details>
<details><summary>Blog Post Detail</summary>
<img src="docs/wireframes/blogpostdetails.png">
</details>
<details><summary>Profile</summary>
<img src="docs/wireframes/profile.png">
</details>
<details><summary>Logout</summary>
<img src="docs/wireframes/logout.png">
</details>
<br>

[Back up](#table-of-content)
