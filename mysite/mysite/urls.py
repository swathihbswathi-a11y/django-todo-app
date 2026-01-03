

from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path
from pages.views import todo, edit_task, update_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('edit/<int:id>/', edit_task),
    path('update/<int:id>/', update_task),
    path('delete/<int:id>/', delete_task),
    path("", lambda request: redirect("/todo/")),

]
