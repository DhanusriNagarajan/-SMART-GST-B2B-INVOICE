from django.urls import path
from .views import get_invoices

urlpatterns = [
    path('invoices/', get_invoices),
]
