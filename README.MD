# WEB ARCHITECTURE

Web architecture involves the design and structure of a web application, including the technologies and components used for both the front-end and back-end. In your described architecture, you have mentioned several technologies. Let's create a high-level overview of a web architecture using these components:

Web Architecture Overview
Front-End:
Vue.js: Vue.js is a progressive JavaScript framework for building user interfaces. It provides a flexible and efficient way to create interactive and responsive web interfaces.

Tailwind CSS: Tailwind CSS is a utility-first CSS framework that simplifies the styling of web components. It allows you to design and style your application with minimal custom CSS.

Pinia: Pinia is a state management system for Vue.js applications. It helps you manage the state of your application and makes it easy to handle data flow between components.

Back-End:
Flask: Flask is a lightweight and micro web framework for Python. It's well-suited for building RESTful APIs and web applications. You can use Flask to handle HTTP requests, routing, and business logic.

Minio: Minio is an open-source object storage server compatible with Amazon S3. It can be used to store and serve large amounts of unstructured data, such as images, videos, and documents.

Schedule: The "schedule" you mentioned likely refers to a task scheduling system. You can use libraries like Celery or APScheduler to schedule and automate background tasks, such as data processing, notifications, and more.

Database: You didn't specify the type of database, but you can choose a database that fits your application's needs. Common choices include PostgreSQL, MySQL, or NoSQL databases like MongoDB, depending on your data storage and retrieval requirements.

Communication:
APIs: The front-end communicates with the back-end through APIs (Application Programming Interfaces). Flask will expose RESTful or GraphQL APIs for the Vue.js front-end to interact with.

Database Connection: Your Flask application will connect to the database to store and retrieve data.

Minio Integration: Flask can integrate with Minio to store and serve files, such as user uploads or other assets.

Deployment:
Web Server: Deploy your Flask back-end on a web server like Nginx or Gunicorn. Configure it to route incoming HTTP requests to your Flask application.

Front-End Hosting: Deploy your Vue.js application on a web hosting service or a content delivery network (CDN) for fast and reliable access.

Database Hosting: Host your chosen database on a suitable database hosting service or on your own servers.

Minio Setup: Set up and configure Minio on your servers or use a managed Minio service if available.

Security:
Implement security measures such as authentication and authorization for user access to your web application and data.

Use HTTPS to encrypt data transmitted between the client and server.

Secure your Minio instance and database with proper access control and encryption.

This architecture provides a high-level overview of how the components you mentioned can be structured to create a web application. Depending on your specific project requirements, you may need to make adjustments and consider additional technologies and components.

## Features

#### Registration Page

![Registration Page](images/register.png?raw=true "Registration Page")
![Registration Page](images/register2.png?raw=true "Registration Page")

#### Login Page

![Login Page](images/login.png?raw=true "Login Page")

#### Home Page

- upload
  ![List of project](images/upload.png?raw=true "List of project")
- Tweets
  ![Added new project](images/tweet.png?raw=true "Added new project")
- Likes
  ![Edit Project](images/likes.png?raw=true "Edit Project")

#### Leaderboard page

- List of tasks
  ![List of tasks](images/leaderboard.png?raw=true "List of tasks")

#### Logout

Logout
![Added new task](images/logout.png?raw=true "Added new task")
Logout

![Edit task](images/logout2.png?raw=true "Edit task")
