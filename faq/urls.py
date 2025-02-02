from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, homepage, add_faq, edit_faq, delete_faq

# Register the API viewset router for the FAQ endpoint
router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    path('', homepage, name='homepage'),  # Homepage with language selection
    path('faq/add/', add_faq, name='add_faq'),  # Add FAQ
    path('faq/edit/<int:faq_id>/', edit_faq, name='edit_faq'),  # Edit FAQ
    path('faq/delete/<int:faq_id>/', delete_faq, name='delete_faq'),  # Delete FAQ
]
