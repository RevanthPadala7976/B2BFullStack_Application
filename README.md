# B2B Data Catalog Application

This project is a B2B data catalog application that allows business users to log in, view a list of available products, and search/filter the products by name or category. The application includes both frontend and backend components, with a focus on user authentication and responsive design.

## Features

- User authentication using JWT tokens
- Display a list of products with details
- Search and filter functionality for products
- Responsive design for different devices

## Tech Stack

- Frontend: React, SCSS
- Backend: FastAPI, SQLAlchemy, MySQL
- Authentication: OAuth2 with JWT tokens

## Prerequisites

- Node.js and npm
- Python 3.8 or higher
- MySQL

## Getting Started

Follow these instructions to set up and run the application locally.

### Backend Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/b2b-data-catalog.git
cd b2b-data-catalog/b2b-data-catalog-api
```
## Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
## Install the required Python packages
```bash
pip install -r requirements.txt
```
## Set up the MySQL database
- Create a new MySQL database.
- Update the `Database_URL` in the `models.py` file with your database credentials.

## Run the database migrations
```bash
python models.py
```
## Start the backend server
```bash
uvicorn main:app --reload
```
The backend server will be running at http://127.0.0.1:8000.


