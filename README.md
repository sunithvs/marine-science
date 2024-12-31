# Marine Science Conference Management System

A Django-based web application for managing marine science conference registrations, abstract submissions, and payments. The system provides a complete solution for conference organization, including user authentication, payment processing, and content management.

## Features

- User registration and authentication system
- Abstract submission and management
- Payment integration for conference registration
- Admin dashboard for managing submissions
- Responsive design with multiple template themes
- Docker containerization for easy deployment
- Nginx configuration for production deployment
- Multi-environment support (development and production)

## Tech Stack

- Django
- PostgreSQL (configured via Docker)
- Nginx
- Docker & Docker Compose
- Bootstrap
- jQuery
- Various frontend libraries (AOS, Swiper, GLightbox, etc.)

## Project Structure

```
sunithvs-marine-science/
├── apps/
│   ├── auth_login/      # Authentication & user management
│   ├── base/            # Core functionality & utilities
│   ├── payment/         # Payment processing
│   ├── maricon/         # Conference management
│   └── home/           # Main website content
├── config/             # Project configuration
│   └── settings/       # Environment-specific settings
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── nginx/             # Nginx configuration
└── scripts/           # Utility scripts
```

## Prerequisites

- Docker and Docker Compose
- Python 3.x (for local development)
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sunithvs-marine-science
```

2. Create environment file:
```bash
cp env.example .env
```
Edit `.env` with your configuration values.

3. Build and start the containers:

For development:
```bash
docker-compose up --build
```

For production:
```bash
docker-compose -f docker-compose-prod.yml up --build
```

## Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Docker Deployment

The project includes two Docker Compose configurations:

- `docker-compose.yml`: Development environment
- `docker-compose-prod.yml`: Production environment with Nginx

### Production Deployment

1. Configure your environment variables in `.env`
2. Build and start the production containers:
```bash
docker-compose -f docker-compose-prod.yml up --build -d
```

## Available Commands

- Run linting:
```bash
python manage.py lint
```

- Collect static files:
```bash
python manage.py collectstatic
```

## Project Components

### Templates
- `new_maricon/`: New conference theme templates
- `maricon/`: Original conference templates
- `home/`: Main website templates
- `payment/`: Payment processing templates

### Static Files
- Vendor libraries in `static/assets/vendor/`
- Custom styles in `static/css/`
- JavaScript files in `static/js/`
- Conference documents in `static/doc/`

## Security

- Configure `settings/prod.py` for production deployment
- Update `SECRET_KEY` in environment variables
- Set up proper SSL/TLS in Nginx configuration
- Configure proper database credentials
- Set up backup systems for the database
