
from django.urls import path
from toDo_app.views import AddTodo, DeleteAll, DeleteItem, TodoView
urlpatterns = [

    path('addTodo/', AddTodo.as_view()),
    path('', TodoView.as_view()),
    path('deleteTodo/<int:todo_id>/',DeleteItem.as_view()),
    path('deleteAll/', DeleteAll.as_view())


]
