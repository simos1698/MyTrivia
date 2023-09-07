from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('questions.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('django_registration.backends.one_step.urls')),
]
