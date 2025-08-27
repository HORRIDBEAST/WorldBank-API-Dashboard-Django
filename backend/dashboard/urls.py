from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('api/countries/', views.get_countries, name='api_countries'),
    path('api/gdp-data/', views.get_gdp_data, name='api_gdp_data'),
    path('api/population-data/', views.get_population_data, name='api_population_data'),
    # NEW ENDPOINTS
    path('api/climate-data/', views.get_climate_data, name='api_climate_data'),
    path('api/education-data/', views.get_education_data, name='api_education_data'),
    path('api/health-data/', views.get_health_data, name='api_health_data'),
    path('api/test/', views.test_worldbank_api, name='api_test'),  # Debug endpoint
]