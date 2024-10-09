# volunteer/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vol_app.urls')),  # This will allow access to API endpoints under /api/
]


