from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from .models import Todo

# Create your views here.
class AddTodo(View):
    def post(self,request):
        Todo(text = request.POST["text"]).save()
        return HttpResponseRedirect('/')

class TodoView(View):
    def get(self, request):
        toDo_list = Todo.objects.all()
        return render(request, 'toDo_app.html', {'listItem' :toDo_list })

class DeleteItem(View):
    def post(self, request, todo_id):
        Todo.objects.get(id= todo_id).delete()
        return HttpResponseRedirect('/')

class DeleteAll(View):

    def post(self, request):
        Todo.objects.all().delete()
        return HttpResponseRedirect('/')
