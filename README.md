# Vibe Coding Backend - Flight Booking System

This is a FastAPI backend for a flight booking system. It uses MongoDB for data storage and supports user login and signup.

## Features

-   User signup
-   User login
-   MongoDB integration

## Setup

1. Create a `.env` file with your MongoDB connection string.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`

## Endpoints

-   `POST /signup` - Register a new user
-   `POST /login` - Authenticate a user

## Environment Variables

-   `MONGO_URL`: MongoDB connection string
