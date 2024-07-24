# Technology Stacks MVP

## MVP Description

Building an identical CRUD task-app in each one of my current stacks. This project will build understanding in these technologies and serve as a blueprint for more complex processes.

## Stacks

- Flask - React
- Express - React
- Spring Boot - React
- NestJS - React
- NextJS
- Express - Angular
- Django
- HTML, CSS, and JavaScript

## App Plan

### Backend

- URL endpoint to test access
- A value passed to the frontend statically (without database access)
- A create endpoint
- A read endpoint
- An update endpoint
- A delete endpoint

### Frontend

- A form page with a CRUD form
- Dynamic display of todo items
- Buttons to create, update, and delete

### Database

- Filled with one value automatically
- Extremely simple design

Example:

```sql
Table todos {
	primary_key: number,
	text: string
}
```

# Notes
- Identical App
- No Styling
- Have frontends/backends and databases self-contained and automatically interchangeable

# Additional Technology
- Docker
- AWS Services
- PostgreSQL
- Redis
- Heroku

# Specifics
- Serverless Technology
  - AWS Elastic Beanstalk
  - AWS S3
  - AWS Lambda
  - AWS ECR
  - AWS ECS
  - AWS EC2

# API Design
- **http**
  ```plaintext
  GET /helloworld
  GET /
  GET /todo
  POST /todo
  PUT /todo/:id
  DELETE /todo/:id

