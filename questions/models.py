from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Question(models.Model):
  categories = (
    ("geography", "Geography"),
    ("entertainment", "Entertainment"),
    ("history", "History"),
    ("literature", "Art & Literature"),
    ("science", "Science & Nature"),
    ("sports", "Sports & Leisure")
  )

  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
  )
  
  category = models.CharField(max_length=32, choices= categories)
  question = models.CharField(max_length=255)
  answer = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.question}"

  def formatted_category(self):
    return dict(Question.categories)[self.category]

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)