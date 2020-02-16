from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

from . import views

import entries.urls as entries_urls

app_name = 'entries'
urlpatterns = [
    path('<slug:entry_slug>', views.index, name='index'),
]
