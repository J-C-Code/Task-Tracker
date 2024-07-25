from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date, timedelta
from .forms import TaskForm
from django.urls import reverse_lazy
# Create your views here.


@login_required
def Home(request):
    today = date.today()  # Get today's date
    end_date = today + timedelta(days=10000)  # Calculate end date (5 days from today)
    
    # Get the logged-in user
    user = request.user
    
    # Filter tasks by due date range and logged-in user
    tasks = models.Task.objects.filter(
        task_due__range=(today, end_date),
        author=user,
        task_complete = False
    ).order_by('task_due')
    
    return render(request, "tasktracking/home.html", {'tasks': tasks})

@login_required
def History(request):
    user = request.user

    tasks = models.Task.objects.filter(
        author=user,
        task_complete = True
    ).order_by('task_due')
    return render(request, "tasktracking/task_history.html", {'tasks': tasks})

@require_POST
def update_task_status(request):
    task_id = request.POST.get('task_id')
    task_complete = request.POST.get('task_complete') == 'on'  # Checkbox returns 'on' if checked

    try:
        task = models.Task.objects.get(pk=task_id)
        task.task_complete = task_complete
        task.save()
    except models.Task.DoesNotExist:
        pass  # Handle the error as appropriate (e.g., logging)

    return redirect('task-home')  # Redirect to the home page or another view

@require_POST
def update_task_status_history(request):
    task_id = request.POST.get('task_id')
    task_complete = request.POST.get('task_complete') == 'on'  # Checkbox returns 'on' if checked

    try:
        task = models.Task.objects.get(pk=task_id)
        task.task_complete = task_complete
        task.save()
    except models.Task.DoesNotExist:
        pass  # Handle the error as appropriate (e.g., logging)

    return redirect('task-history')  # Redirect to the home page or another view


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy('task-home')
    template_name = 'tasktracking/task_confirm_delete.html'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    form_class = TaskForm  # Use the custom form

    template_name = 'tasktracking/task_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-home')