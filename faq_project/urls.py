from django.contrib import admin
from django.urls import path, include
from faq.views import signup_view

# URL patterns for routing requests in the Django project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('faq.urls')),  # Includes all FAQ-related URLs (homepage & FAQ section)
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in authentication URLs (login/logout, password management)
    path('signup/', signup_view, name='signup'),  # Custom signup page view
]
