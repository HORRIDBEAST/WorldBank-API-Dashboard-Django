# World Bank Data Dashboard

A comprehensive Django web application that displays interactive visualizations of World Bank data, featuring user authentication and dynamic filtering capabilities.

## 🚀 Live Demo

**Deployed URL**: [https://worldbank-api-dashboard-django-2.onrender.com/]

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Architecture](#architecture)
- [Probable Issues & Solutions](#probable-issues--solutions)
- [Contributing](#contributing)

## ✨ Features

### 🔐 Authentication System
- **User Registration**: New users can create accounts
- **User Login/Logout**: Secure authentication using Django's built-in system
- **Protected Routes**: Dashboard access restricted to authenticated users only

### 📊 Interactive Dashboard
- **Multiple Chart Types**: Line charts, bar charts, and area charts
- **Real-time Data**: Dynamic data fetched from Django backend APIs
- **Interactive Filtering**: 
  - Filter by country selection
  - Date range filtering (year-based)
  - Category-based filtering
- **Responsive Design**: Mobile-friendly interface

### 📈 Data Visualization Categories
1. **Economic Indicators**
   - GDP (Current US$)
   - GDP Growth Rate
   
2. **Population Statistics**
   - Total Population
   - Population Growth

3. **Climate Data**
   - CO2 Emissions
   - Temperature anomalies

4. **Education Metrics**
   - Literacy rates
   - School enrollment

5. **Health Indicators**
   - Life expectancy
   - Healthcare statistics

## 🛠 Technology Stack

### Backend
- **Django 4.2.7**: Web framework
- **Django REST Framework 3.14.0**: API development
- **SQLite**: Database (development/production)
- **Gunicorn**: WSGI server for production

### Frontend
- **HTML5/CSS3**: Structure and styling
- **JavaScript (Vanilla)**: Interactive functionality
- **Chart.js**: Data visualization library
- **Bootstrap 5**: Responsive UI components

### Deployment
- **Render**: Cloud hosting platform
- **WhiteNoise**: Static file serving
- **Gunicorn**: Production WSGI server

### External APIs
- **World Bank API**: Real-time data source

## 📁 Project Structure

```
backend/
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore file
├── dashboard/                   # Main Django app
│   ├── admin.py                # Django admin configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models
│   ├── serializers.py          # DRF serializers
│   ├── urls.py                 # App URL patterns
│   └── views.py                # API views and logic
├── dashboard_project/           # Django project settings
│   ├── settings.py             # Project configuration
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── __init__.py
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── Procfile                    # Render deployment config
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── dashboard/
│   │   └── dashboard.html     # Main dashboard
│   └── registration/
│       ├── login.html         # Login page
│       └── register.html      # Registration page
└── static/                     # Static files (CSS, JS, images)
```

## 🔌 API Endpoints

### Authentication Endpoints
- `GET/POST /login/` - User login
- `POST /logout/` - User logout  
- `GET/POST /register/` - User registration

### Dashboard Endpoints
- `GET /` - Main dashboard (authenticated users only)

### Data API Endpoints
- `GET /api/countries/` - Fetch available countries
- `GET /api/gdp-data/` - GDP data with country/year filtering
- `GET /api/population-data/` - Population statistics
- `GET /api/climate-data/` - Climate and environmental data
- `GET /api/education-data/` - Education indicators
- `GET /api/health-data/` - Health statistics
- `GET /api/test/` - Debug endpoint for World Bank API testing

### API Parameters
Most data endpoints support the following query parameters:
- `countries`: Comma-separated country codes (e.g., `US,IN,CN`)
- `start_year`: Starting year for data range
- `end_year`: Ending year for data range

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your configurations
   # Add SECRET_KEY, DEBUG settings, etc.
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser  # Optional: Create admin user
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 🌐 Deployment

### Render Deployment

This application is configured for deployment on Render with the following files:

#### `Procfile`
```
web: gunicorn dashboard_project.wsgi:application
```

#### `runtime.txt`
```
python-3.11.0
```

#### Environment Variables (Set in Render Dashboard)
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-render-app.onrender.com
```

### Deployment Steps

1. **Connect Repository**: Link your GitHub repository to Render
2. **Configure Build Settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn dashboard_project.wsgi:application`
3. **Set Environment Variables**: Add necessary environment variables in Render dashboard
4. **Deploy**: Render will automatically build and deploy your application

## 🏗 Architecture

### Backend Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Django Views   │    │  World Bank API │
│   (HTML/JS)     │◄──►│   & API Layer    │◄──►│    External     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   SQLite DB      │
                       │   (Data Cache)   │
                       └──────────────────┘
```

### Data Flow
1. **User Authentication**: Django's built-in auth system manages user sessions
2. **Data Fetching**: Views fetch data from World Bank API and cache in local database
3. **API Serialization**: Django REST Framework serializes data for frontend consumption
4. **Frontend Rendering**: JavaScript processes API responses and renders charts using Chart.js

### Security Features
- CSRF protection on all forms
- User authentication required for dashboard access
- Input validation and sanitization
- Secure session management

## ⚠️ Probable Issues & Solutions

### Common Issues

#### 1. **World Bank API Rate Limiting**
**Issue**: External API may have rate limits
**Solution**: 
- Implement caching mechanism in Django models
- Add exponential backoff for API requests
- Store frequently accessed data in local database

#### 2. **Static Files Not Loading (Production)**
**Issue**: CSS/JS files not served correctly on Render
**Solution**: 
- Ensure `STATIC_ROOT` is configured in settings.py
- Run `python manage.py collectstatic` during deployment
- WhiteNoise is configured for static file serving

#### 3. **CORS Issues**
**Issue**: Frontend API calls blocked by CORS policy
**Solution**: 
- `django-cors-headers` is installed and configured
- Add your Render domain to `CORS_ALLOWED_ORIGINS`

#### 4. **Database Migrations**
**Issue**: Database not properly initialized on deployment
**Solution**: 
- Add migration command to Render build process
- Ensure all migrations are committed to repository

#### 5. **Environment Variables**
**Issue**: Missing SECRET_KEY or other environment variables
**Solution**: 
- Use `.env.example` as reference
- Set all required variables in Render dashboard
- Use `python-decouple` for environment variable management

### Debug Endpoints

Use `/api/test/` endpoint to verify World Bank API connectivity:
```bash
curl https://your-app.onrender.com/api/test/
```

### Performance Optimization

1. **Database Indexing**: Add indexes to frequently queried fields
2. **API Caching**: Implement Redis for API response caching
3. **Frontend Optimization**: Minify CSS/JS files for production
4. **Database Connection Pooling**: Use connection pooling for better performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is developed for educational purposes as part of the Full Stack Developer Intern application at DeepQ-AI.

## 🔗 Links

- **Live Application**: [Your Render URL]
- **GitHub Repository**: [Your GitHub URL]
- **World Bank API Documentation**: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392

---

### Assignment Completion Checklist ✅

- [x] Django backend with interactive dashboard
- [x] At least two different chart types (line charts, bar charts)
- [x] Dynamic data fetched from backend API
- [x] Filtering capabilities (country, date range, category)
- [x] User authentication (login/logout)
- [x] Restricted dashboard access for logged-in users
- [x] World Bank Open Data integration
- [x] Deployment on Render
- [x] Comprehensive README documentation

**Submission Date**: August 28, 2025
**Submitted to**: DeepQ-AI Full Stack Developer Intern Position
