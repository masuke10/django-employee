# Employee Management System API

A Django REST API for managing employees, departments, attendance, and performance reviews.

## Features

- JWT Authentication
- Employee Management
- Department Management
- Attendance Tracking
- Performance Reviews
- API Documentation with Swagger/ReDoc
- Filtering, Searching, and Pagination

## Tech Stack

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger/ReDoc for API documentation

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd employee_management_system
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
# Update the .env file with your configurations
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Seed sample data (optional):
```bash
python manage.py seed_data
```

8. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST `/api/token/` - Obtain JWT token
- POST `/api/token/refresh/` - Refresh JWT token

### Departments
- GET `/api/v1/departments/` - List departments
- POST `/api/v1/departments/` - Create department
- GET `/api/v1/departments/{id}/` - Retrieve department
- PUT `/api/v1/departments/{id}/` - Update department
- DELETE `/api/v1/departments/{id}/` - Delete department

### Employees
- GET `/api/v1/employees/` - List employees
- POST `/api/v1/employees/` - Create employee
- GET `/api/v1/employees/{id}/` - Retrieve employee
- PUT `/api/v1/employees/{id}/` - Update employee
- DELETE `/api/v1/employees/{id}/` - Delete employee

### Documentation
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Environment Variables

See `.env.example` for required environment variables.

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. Obtain token:
```bash
curl -X POST http://localhost:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "your_username", "password": "your_password"}'
```

2. Use token in requests:
```bash
curl http://localhost:8000/api/v1/employees/ \
    -H "Authorization: Bearer your.access.token"
```

## Development

1. Run tests:
```bash
python manage.py test
```

2. Check code style:
```bash
flake8
```

## License

MIT License 