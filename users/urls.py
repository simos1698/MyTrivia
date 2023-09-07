from django.urls import path
from . import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('users/<str:username>', views.user_details, name="user_details"),
    path('mylist', views.mylist, name="mylist"),
    path('register/',
        RegistrationView.as_view(success_url='/'),
        name='register'),
    path('logout/', views.loggedout, name='logged-out'),
]