from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import ParticipantDetailsView, EventsRegisterView
from . import views

app_name = 'app'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('details/', views.ParticipantDetailsView, name='details'),
    path('events/', views.EventsRegisterView, name='events'),
    path('events/samwaad', views.samvaad, name='samwaad'),
    path('events/ei', views.ei, name='ei'),
]