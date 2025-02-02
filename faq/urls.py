from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet
from django.urls import path
from . import views
from .views import homepage, add_faq, edit_faq

# Register the API viewset router for the FAQ endpoint
router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    # Homepage view with language selection
    path('', homepage, name='homepage'),  
    
    # FAQ CRUD actions
    path('faq/add/', add_faq, name='add_faq'),
    path('faq/edit/<int:faq_id>/', edit_faq, name='edit_faq'),
    path('faq/delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
    
]
