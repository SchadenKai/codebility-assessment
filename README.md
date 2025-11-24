## E-Commerce Fullstack Application
Features a basic e-commerce fullstack web application. You can view the codebase for this [here](/fullstack/).

## Features:
- User Management, Authentication, and Authorization System
- Produts Management System for admin users
- Cart feature for basic users
- Product List page

## Tech Stack
### Backend:
- FastAPI
- FastAPI Users (for User management)
- SQLAlchemy (ORM)
- Alembic (database migration tool)
### Frontend:
- NextJS
- SchadcnUI (component library)
- TailwindCSS
- Tanstack: React Query (for API calling)

## Codebase Structure
The codebase is separated into two separate projects. One is a FastAPI application that serves as the api server of the project, which can be viewed [here](/fullstack/backend/). And a NextJS application that serves as the client side application / frontend application of the project, which can be viewed [here](/fullstack/web/).

The backend application follows a structure called layered architecture where the services, which contains the business logic, the repository, which contains the database-interacting functions, and the routes are separated from each other by layers.