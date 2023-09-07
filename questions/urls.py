from django.urls import path
from . import views

urlpatterns = [
    path('questions/<int:id>', views.question_profile, name="question_profile"),
    path('questions/<str:category>', views.questions, name='questions'),
    path('random_question', views.random_question, name="random_question"),
    path('add_question', views.add_question, name="add_question"),
]