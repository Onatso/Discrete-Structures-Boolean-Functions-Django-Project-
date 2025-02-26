from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,View


# Create your views here.

class TaskList(ListView):

    model = Task

    ordering = 'id'

    template_name = 'task_list.html'

    context_object_name = 'Tasks'

    #paginate_by = 2

class TaskDetail(DetailView):
    model = Task

    template_name = "task_detail.html"

    context_object_name = 'task'