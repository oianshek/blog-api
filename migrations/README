# Blog API

## Overview

The **Blog API** is a RESTful web service designed for managing blog posts. It provides CRUD operations for blog posts, advanced search capabilities, statistics per user, and supports pagination. The API is built using Python's FastAPI framework and uses PostgreSQL as the database backend. Docker is used to containerize the application for easy deployment.

---

## Features

1. **CRUD Operations**:
   - `GET /posts`: Retrieve all blog posts with optional pagination.
   - `GET /posts/{id}`: Fetch a specific blog post by its ID.
   - `POST /posts`: Create a new blog post.
   - `PUT /posts/{id}`: Update an existing blog post.
   - `DELETE /posts/{id}`: Delete a blog post.

2. **Search**:
   - `GET /posts/search`: Search blog posts by title or content.

3. **Statistics**:
   - `GET /posts/statistics/{user_id}`: Get the average number of posts per month for a specific user.

4. **Pagination**:
   - Supports customizable pagination for `GET /posts`.

---

## Project Structure

```plaintext
blog-api/
├── app/
│   ├── core/           # Application configuration and utilities
│   ├── dependency/     # Dependency injection
│   ├── exception/      # Custom exceptions
│   ├── model/          # Database models
│   ├── repository/     # Data access layer
│   ├── router/         # API routes
│   ├── schema/         # Request/response schemas
│   ├── service/        # Business logic
│   ├── utils/          # Helper functions
│   ├── __init__.py
│   └── main.py         # Application entry point
├── migrations/         # Alembic migrations
├── test/               # Unit and integration tests
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── alembic.ini         # Alembic configuration
├── docker-compose.yml  # Docker Compose configuration
└── README.md           # Project documentation
