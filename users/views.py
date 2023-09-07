import json
from re import template
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from questions.models import Question, Favorite

def main(request):
    print(request.user)
    template = loader.get_template('main.html')
    questions = Question.objects.order_by('-id').all()[:5]
    if request.user.is_authenticated : favorites = Favorite.objects.filter(user=request.user) 
    else: favorites = []

    # The user ADDS a favorite a question
    if request.method == 'POST':
        if request.user.is_authenticated:
            question_id = json.loads(request.body)["question_id"]
            question = Question.objects.get(id=question_id)

            f = Favorite(user=request.user, question=question)
            print("New favorite object created:", f.question, "favorited by user", f.user)
            f.save()

            return JsonResponse({'success': True})
        else:
            messages.info(request, "You need to be logged in to add a question to your favorites.")
            return redirect('login')

    # The user REMOVES a favorite question
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            question_id = json.loads(request.body)["question_id"]
            question = Question.objects.get(id=question_id)

            favorites = Favorite.objects.filter(user=request.user, question=question)
            if favorites.exists():
                print("New favorite object deleted:", favorites[0].question, "favorited by user", favorites[0].user)
                favorites.delete()

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        else:
            messages.info(request, "You need to be logged in to add a question to your favorites.")
            return redirect('login')
    
    context = {'questions': questions, 'favorites': [favorite.question for favorite in favorites], }
    
    return HttpResponse(template.render(context, request))

def users(request):
    template = loader.get_template('users.html')
    myusers = User.objects.all().values()

    context = {'myusers': myusers}

    return HttpResponse(template.render(context, request))

def user_details(request, username):
    template = loader.get_template('user_details.html')
    
    user = User.objects.get(username = username)
    questions = Question.objects.filter(user=user)

    context = {'user' : user, 'questions':questions}
    return HttpResponse(template.render(context, request))

def mylist(request):
    template = loader.get_template('mylist.html')

    if not request.user.is_authenticated:
        messages.info(request, "You need to be logged in to view your list.")
        return redirect('login')
    
    favorites = Favorite.objects.filter(user = request.user)
    questions = [fav.question for fav in favorites]

    context = {'questions': questions}
    return HttpResponse(template.render(context, request))

def register(request):
    form = UserCreationForm()
    context = {form}
    return HttpResponse(template.render(context, request))

def loggedout(request):
    logout(request)
    template = loader.get_template('logged_out.html')
    return HttpResponse(template.render({}, request))
