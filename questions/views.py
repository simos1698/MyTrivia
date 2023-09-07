import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.template import loader
from django.shortcuts import render, redirect
from .models import Question, Favorite
from .forms import QuestionForm
from random import choice

@csrf_exempt
def questions(request, category):
    template = loader.get_template('questions.html')
    questions = Question.objects.all()
    if request.user.is_authenticated : favorites = Favorite.objects.filter(user=request.user) 
    else: favorites = []

    # The user ADDS a favorite a question
    if request.method == 'POST':
        print("new post method requested")
        if request.user.is_authenticated:
            question_id = json.loads(request.body)["question_id"]
            question = Question.objects.get(id=question_id)

            f = Favorite(user=request.user, question=question)
            print("New favorite object created:", f.question, "favorited by user", f.user)
            f.save()

            return JsonResponse({'success': True})
        else:
            messages.info(request, "You need to be logged in to add a question to your favorites.")
            return JsonResponse({'success': False})

    # The user REMOVES a favorite question
    if request.method == 'DELETE':
        print("new post method requested")
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
            return JsonResponse({'success': False})

    context = {
        'questions': questions, 
        'favorites': [favorite.question for favorite in favorites], 
        'categories': dict(Question.categories),
        'filter': category
    }
    return HttpResponse(template.render(context, request))

def question_profile(request, id):
    template = loader.get_template('question_profile.html')

    question = Question.objects.get(id=id)
    context = {'question' : question}

    return HttpResponse(template.render(context, request))

def random_question(request):
    template = loader.get_template('question_profile.html')
    
    question = choice(Question.objects.all())
    context = {'question' : question}

    return HttpResponse(template.render(context, request))

def add_question(request):

    if not request.user.is_authenticated:
        messages.info(request, "You need to be logged in to add a question")
        return redirect('login')
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']

            Question.objects.create(user = request.user, category= category, question=question, answer=answer)
            return redirect('questions/all')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})