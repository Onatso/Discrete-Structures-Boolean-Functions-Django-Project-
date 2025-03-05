from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from pprint import pprint
from datetime import datetime
# Create your views here.

class TaskList(LoginRequiredMixin,ListView):

    model = Task

    ordering = 'id'

    template_name = 'task_list.html'

    context_object_name = 'Tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.utcnow()
        pprint(context)
        return context

    paginate_by = 3


class TaskDetail(LoginRequiredMixin,DetailView,):
    model = Task

    template_name = "task_detail.html"

    context_object_name = 'task'