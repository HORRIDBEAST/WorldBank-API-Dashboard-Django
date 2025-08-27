# World Bank Interactive Data Dashboard

## 📊 Live Application

**URL:** **[[YOUR LIVE URL HERE](https://worldbank-api-dashboard-django-2.onrender.com/)]** _(e.g., https://your-app-name.onrender.com)_

---

## 🚀 Project Overview

This full-stack web application provides an interactive and dynamic dashboard for visualizing global development data sourced directly from the World Bank. Built with a robust Django backend and a classic HTML/CSS/JavaScript frontend, the application allows users to explore complex datasets through intuitive charts and filters. The project fulfills all requirements of the Full Stack Developer Intern assignment, demonstrating proficiency in backend development, API integration, frontend data visualization, and cloud deployment.



[Image of the dashboard application interface]


## ✨ Key Features

* **Secure User Authentication**: Full registration, login, and logout functionality using Django's built-in session authentication system. The dashboard is protected and accessible only to authenticated users.
* **Dynamic, Multi-Category Dashboard**: Users can switch between different data categories (Economic, Climate, Education, Health) to explore a wide range of global indicators.
* **Interactive Data Visualizations**: The dashboard renders multiple chart types (Line, Bar, Doughnut) for each data category, providing different perspectives on the data (e.g., trends over time vs. latest-year comparisons).
* **Live Data Filtering**: All charts can be dynamically updated by filtering data based on a selection of countries and a specified date range.
* **Real-time API Integration**: Data is fetched live from the World Bank Open Data API, ensuring the visualizations are always up-to-date.
* **Responsive Design**: The user interface is built with Bootstrap, making it accessible and functional across various devices and screen sizes.
* **Cloud Deployed**: The application is deployed and publicly accessible on Render, configured for production use with Gunicorn and WhiteNoise.

---

## 🛠️ Technology Stack

This project leverages a powerful and reliable stack to deliver a seamless user experience.

* **Backend**:
    * **Django (4.2.7)**: The high-level Python web framework used for the entire backend logic, user authentication, and API serving.
    * **Django REST Framework (DRF)**: A powerful toolkit for building robust and secure Web APIs.
    * **Gunicorn**: A production-ready WSGI HTTP server for deploying the Django application.
* **Frontend**:
    * **HTML5 & CSS3**: For the structure and styling of the web pages.
    * **JavaScript (ES6+)**: For handling user interactions, API calls (`fetch`), and dynamically rendering charts.
    * **Chart.js**: A modern and popular charting library for creating beautiful, interactive, and responsive data visualizations.
    * **Bootstrap**: A leading CSS framework for building responsive, mobile-first websites.
* **Database**:
    * **SQLite**: The default Django database used for local development and storing user authentication data.
* **Deployment**:
    * **Render**: A modern cloud platform for deploying web applications.
    * **WhiteNoise**: For efficiently serving static files (CSS, JS) in a production environment.
* **Data Source**:
    * **World Bank Open Data API**: The official source for all visualized data.

---

## 🏗️ Architecture and Design

The application follows a traditional monolithic architecture, where the Django backend serves both the HTML templates and the JSON data for the charts.

1.  **User Authentication**: Django's built-in `django.contrib.auth` system manages user models, sessions, and password security. The `@login_required` decorator protects the main dashboard view, while DRF's `IsAuthenticated` permission class secures all API endpoints.
2.  **Frontend Rendering**: Django's templating engine renders the `base.html` structure and the initial dashboard layout. All further dynamic behavior is handled by client-side JavaScript.
3.  **API Layer**: A set of API endpoints (e.g., `/api/gdp-data/`, `/api/climate-data/`) are defined using Django REST Framework. These endpoints are responsible for:
    * Receiving requests from the frontend with filter parameters (countries, years, indicator).
    * Calling a dedicated `WorldBankAPI` helper class to fetch the corresponding data from the external World Bank API.
    * Processing and formatting the raw data into a clean JSON structure suitable for Chart.js.
    * Returning the JSON response to the frontend.
4.  **Client-Side Logic**: The `dashboard.html` template contains extensive JavaScript code that:
    * Handles user interactions with the category and filter dropdowns.
    * Constructs and sends `fetch` requests to the Django backend's API endpoints based on user selections.
    * Manages the UI state, such as showing and hiding different chart sections and displaying a loading indicator.
    * Parses the JSON response from the backend and uses Chart.js to render or update the charts on the page.

---

## 🚀 Local Development Setup

Follow these instructions to get the project running on your local machine.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* A virtual environment tool (like `venv`)

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone [YOUR GITHUB REPO URL HERE]
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    * Create a `.env` file in the project root directory.
    * Add the following content. For local development, these defaults are sufficient.
    ```env
    SECRET_KEY=django-insecure-local-development-key
    DEBUG=True
    ```

5.  **Run Database Migrations**
    * This will create the `db.sqlite3` file and set up the necessary tables for user accounts.
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional)**
    * This allows you to access the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

8.  **Access the Application**
    * Open your web browser and navigate to `http://127.0.0.1:8000`.
    * You will be redirected to the login page. You can register a new user or log in with the superuser credentials you created.

---

## 📡 API Endpoints

All data endpoints are protected and require the user to be authenticated.

| Method | Endpoint                    | Description                                                                                              |
| :----- | :-------------------------- | :------------------------------------------------------------------------------------------------------- |
| `GET`  | `/api/countries/`           | Fetches a list of countries from the World Bank API.                                                     |
| `GET`  | `/api/gdp-data/`            | Fetches GDP data for the selected countries and date range.                                              |
| `GET`  | `/api/population-data/`     | Fetches total population data for the selected countries and date range.                                 |
| `GET`  | `/api/climate-data/`        | Fetches climate data (e.g., CO2 emissions). Requires an `indicator` query parameter.                     |
| `GET`  | `/api/education-data/`      | Fetches education data (e.g., literacy rate). Requires an `indicator` query parameter.                   |
| `GET`  | `/api/health-data/`         | Fetches health data (e.g., life expectancy). Requires an `indicator` query parameter.                    |

---

## 🧐 Known Issues & Future Improvements

* **Potential for Slow API Responses**: Since the application fetches data live from the World Bank API, initial load times or filter updates can sometimes be slow depending on the external API's performance.
    * **Improvement**: Implement a caching layer (e.g., with Redis) to store frequently requested data, significantly speeding up response times.
* **Limited Data Caching**: The application does not store the fetched World Bank data in its own database. The `WorldBankData` model is defined but currently unused in the data-fetching logic.
    * **Improvement**: Create a background task (e.g., using Celery) to periodically fetch and store World Bank data in the local database. This would make the application more resilient to external API outages and faster for the end-user.
* **Frontend Code in Template**: All JavaScript logic resides within a `<script>` tag in the `dashboard.html` template.
    * **Improvement**: For larger projects, this logic could be moved to separate `.js` files and served as static assets. For even more complex interactivity, migrating the frontend to a dedicated framework like React or Vue.js would be a logical next step.
