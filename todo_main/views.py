from django.http import HttpResponse
from .models import Tasks
from django.shortcuts import redirect, render

# Create your views here.


def task_read(request):
    tasks = Tasks.objects.filter(is_done=False)
    context = {
        "tasks": tasks
    }
    return render(request, "index.html", context)

def task_add(request):
    
    task_name = request.POST.get("task_name")
    Tasks.objects.create(name=task_name)
    return redirect("home")

def task_delete(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect("home")