
from django.urls import path
from toDo_app.views import AddTodo, DeleteAll, DeleteItem, TodoView,Upload

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('addTodo/', AddTodo.as_view()),
    path('', TodoView.as_view()),
    path('deleteTodo/<int:todo_id>/',DeleteItem.as_view()),
    path('deleteAll/', DeleteAll.as_view()),
    path('upload/', Upload.as_view(), name = 'upload')
    #path('imageList/', Image_list.as_view(), name = 'images')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
