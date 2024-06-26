# research_tracker/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('research.urls')),  # Assurez-vous que cette ligne pointe vers 'research.urls'
]
