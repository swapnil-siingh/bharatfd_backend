from django.contrib import admin
from django.urls import path, include
from faq.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faq.urls')),  # Homepage & FAQ URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout URLs
    path('signup/', signup_view, name='signup') # Custom Signup
]
