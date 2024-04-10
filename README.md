# Title: IMDb Movie Stream Platform Project

## Description:
This project is aimed at creating a movie streaming platform similar to IMDb. Users can browse movies, view details about each movie, and stream them online. The platform utilizes Django and Django Rest Framework for backend development, providing RESTful APIs to interact with the database. MySQL is used as the relational database management system to store movie information and user data.

## Technologies Used:
- Python: Python is the primary programming language used for backend development in this project.
- Django: Django is a high-level Python web framework that facilitates rapid development and clean, pragmatic design. It is used for building the backend of the movie streaming platform.
- Django Rest Framework (DRF): DRF is a powerful toolkit for building Web APIs in Django. It is used to create RESTful APIs for communication between the frontend and backend of the platform.
- REST API: Representational State Transfer (REST) is an architectural style for designing networked applications. RESTful APIs are used to allow seamless communication between the client-side and server-side components of the platform.
- MySQL: MySQL is an open-source relational database management system. It is used to store movie information, user data, and other related data in a structured manner.

## Project Structure:
- The project is structured following Django's recommended project layout, with separate directories for settings, URLs, apps, static files, media files and templates.
- Django models are used to define the structure of the MySQL database, including models for WatchList, StreamPlatform, Review, and other relevant entities.
- Django Rest Framework serializers are employed to convert Django model instances into JSON format for API responses.
- Views and URLs are implemented to handle HTTP requests and map them to appropriate controller methods.

## Setup Instructions:
1. Clone the repository from GitHub: https://github.com/nagesh882/MovieStreamPlatformAPI.git
2. Install Python and required dependencies [django, djangorestframework, mysqlclient].
3. Set up a MySQL database and configure the Django settings file accordingly.
4. Run Django migrations to create the necessary database tables.
5. Start the Django development server.

## Contributing:
Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.
