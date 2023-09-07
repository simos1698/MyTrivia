from django.contrib import admin
from .models import Question, Favorite

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ("question", "answer")
  
admin.site.register(Question, UserAdmin)
admin.site.register(Favorite)