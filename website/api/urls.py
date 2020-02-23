from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

from . import views

app_name = 'api'
urlpatterns = [
    path('entries/', views.get_entries, name='get_entries'),
]
