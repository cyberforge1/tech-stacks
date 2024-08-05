# Technology Stacks MVP

## Description

A collection of different tech stacks to build an identical CRUD application with modular frontend, backend, database, and deployment components.

## Tech Stacks

- [x] Flask - React
- [ ] Express - React
- [ ] Spring Boot - React
- [ ] NestJS - React
- [ ] NextJS
- [ ] Express - Angular
- [ ] Django
- [ ] HTML, CSS, and JavaScript

# Project MVP

- Frontend / Backend / Database / Container / Cloud Deployment

## Frontend

- (/) A landing page that contains:
    - value passed from the backend (ex. Home Page)
    - button redirecting to the form page

- (/form) A form page that contains:
    - title	
    - input field
    - ‘add todo’ button
    - dynamic display of todos in the database
    - dynamically rendered ‘update todo’ button
    - dynamically rendered delete todo’ button

## Backend


- URL endpoint to test access (ex. /helloworld)
- A value passed to the frontend directly as a string from the backend (w/o db access)
- Create, read, update and delete endpoints

```http
GET /helloworld
GET /
GET /todo
GET /todo/:id
POST /todo
PUT /todo/:id
DELETE /todo/:id
```

## Database

- Filled with one value automatically 
- Transitioning from a local to a cloud-base database upon deployment
- Either SQL or NoSQL solutions
- Fundamentally simple design

```sql
CREATE TABLE todos ( 
primary_key INT PRIMARY KEY, 
text VARCHAR(255) 
);
```

## Container

Using Docker to:
- create a frontend image (/backend/Dockerfile)
- create a backend image (/frontend/Dockerfile)
- create a Docker compose file (/docker-compose.yml)


## Deployment Strategies

- AWS Elastic Beanstalk 
- Docker - AWS ECR - AWS ECS (Fargate)
- Docker - Kubernetes
- AWS EC2 (Autoscaling and Load Balancing)

# Notes

- Frontends/Backends/Databases self-contained and modular (providing re-use and rapid development)
- No Styling
- Identical Application

# Potential Future Additions

- PostgreSQL
- Redis
- S3
- Mong0DB
- AWS Lambda and API Gateway

## Contact Me
- Visit my [LinkedIn](https://www.linkedin.com/in/obj809/) for more details.
- Check out my [GitHub](https://github.com/cyberforge1) for more projects.
- Or send me an email at obj809@gmail.com
<br />
Thanks for your interest in this project. Feel free to reach out with any thoughts or questions.
<br />
<br />
Oliver Jenkins © 2024
