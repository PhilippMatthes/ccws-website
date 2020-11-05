from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('entries/', views.get_entries, name='get_entries'),
]
