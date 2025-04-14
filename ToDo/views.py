from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView

from ToDo.forms import TaskForm
from ToDo.models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "index.html"

    # add form to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    # handle post from form
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('home'))

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')
    template_name = "edit.html"

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')