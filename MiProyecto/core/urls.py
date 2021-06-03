from django.urls import path
from django.urls import URLPattern
from .views import index, contacto

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto")
]