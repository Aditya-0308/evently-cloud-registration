# Evently – Cloud-Based Event Registration System

## About the Project

Evently is a cloud-based event registration web application developed using Python and Flask. It allows users to explore upcoming events, select events, submit registration details, and receive registration confirmation.

The project demonstrates backend web development and deployment using cloud hosting platforms.

## Features

- Displays six upcoming events.
- Allows users to select an event.
- Provides an online registration form.
- Processes registration submissions.
- Displays registration confirmation.
- Includes an application health-check endpoint.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| HTML/CSS | User interface |
| SQLite | Registration database |
| Gunicorn | WSGI application server |
| GitHub | Source code management |
| AWS Elastic Beanstalk | Cloud deployment |
| Amazon EC2 | Compute infrastructure |
| Amazon S3 | Deployment package storage |
| Render | Additional web hosting |

## AWS Deployment

The application was deployed using AWS Elastic Beanstalk.

Deployment workflow:

1. Develop the Flask application.
2. Prepare the application dependencies.
3. Create a deployment ZIP package.
4. Upload the package to Amazon S3.
5. Configure the Elastic Beanstalk environment.
6. Deploy the application on Amazon EC2.
7. Access the application through its public URL.

## Project Files

- `application.py` – Main Flask application.
- `requirements.txt` – Python dependencies.
- `Procfile` – Application startup configuration.

## Live Demo

[Open Evently](https://evently-cloud-registration.onrender.com)

## Future Enhancements

- Integration with a persistent managed database.
- User authentication.
- Administrator dashboard.
- Email registration notifications.
- Auto Scaling and load balancing.

---

Developed as a cloud computing project.
