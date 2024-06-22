# B2B Data Catalog Application

![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SCSS](https://img.shields.io/badge/SCSS-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)




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
git clone https://github.com/RevanthPadala7976/B2BFullStack_Application.git
cd b2b-data-catalog/b2b-data-catalog-api
```
2. **Create and activate a virtual environment**
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
3. **Install the required Python packages**
```bash
pip install -r requirements.txt
```
4. **Set up the MySQL database**
- Create a new MySQL database.
- Update the `Database_URL` in the `models.py` file with your database credentials.

5. **Run the database migrations**
```bash
python models.py
```
6. **Start the backend server**
```bash
uvicorn main:app --reload
```
The backend server will be running at http://127.0.0.1:8000.

# Running the Application
1. **Access the frontend application**

Open your browser and navigate to http://localhost:3000.

2. **Log in**

Use the following credentials to log in and test the functionalities:

- Username: admin
- Password: admin@123
  
After logging in, you will be able to view and search the product catalog.

# License
This project is licensed under the MIT License.

