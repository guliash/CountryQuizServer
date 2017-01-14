from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import CreateForm
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the questions index")

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            question = Question(name = name, description = description, image = request.FILES['image'], publish_date = timezone.now())
            question.save()
            return HttpResponseRedirect(reverse('questions:question', args=(question.id,)))
    else:
        form = CreateForm()
    return render(request, 'questions/create.html', {'form': form})

@login_required
def question(request, question_id):
    return render(request, 'questions/question.html', {'question': get_object_or_404(Question, pk = question_id)})

@login_required
def all(request):
    return render(request, 'questions/all.html', {'questions': Question.objects.all()})
