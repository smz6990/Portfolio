from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("contact", views.ContactFormView.as_view(), name="contact-form")
]
