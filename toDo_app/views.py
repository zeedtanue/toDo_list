from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.files.storage import FileSystemStorage

from zipfile import ZipFile

from .models import Todo, Images

from .forms import ImageForm

import os


def list_files(dir):
    r = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)
        else:
            return r
    return r
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

class Upload(View):

    def post(self, request):
        url_array = []
        fs = FileSystemStorage()

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imageZip=request.FILES
            print(imageZip['image'])




            with ZipFile(imageZip['image'], 'r') as zip:
                zip.extractall()
                unzip_file= zip.namelist()
                print(unzip_file)



                for files in unzip_file:

                    with open(files, "rb") as file:
                        name = fs.save('read.jpg', file)
                    Images(image = name).save()
                    url_array.append(fs.url(name))
        else:
            form = ImageForm()


        return render(request, 'toDo_app.html', context = {'form': form, 'url':url_array})
