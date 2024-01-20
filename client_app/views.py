from django import forms
from django.db import models
from django.shortcuts import render
from .scripts import chat_gpt_api

class UserInput(models.Model):
    content = models.TextField()

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['content']
        labels = { 'content': '' }

def index(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            messages = [object.content for object in UserInput.objects.all()]
            reply = chat_gpt_api.ask_question(messages)
            return render(request, 'client_app/index.html', {'form': form, 'reply': reply})
    else:
        form = UserInputForm()

    return render(request, 'client_app/index.html', {'form': form, 'reply': ''})

