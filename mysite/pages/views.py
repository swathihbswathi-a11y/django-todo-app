from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

def todo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        messages.success(request, "Task added successfully!")

        return redirect("/todo/")

    tasks = Task.objects.all()

    return render(request, "todo.html", {"tasks": tasks})


def edit_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, "edit.html", {"task": task})


def update_task(request, id):
    task = Task.objects.get(id=id)
    task.title = request.POST.get("title")
    task.save()
    messages.success(request, "Task updated successfully!")
    return redirect("/todo/")


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.warning(request, "Task deleted.")
    return redirect("/todo/")
