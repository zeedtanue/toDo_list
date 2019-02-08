
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, DetailView,
                                CreateView, DeleteView
                                , UpdateView, ListView)
from . import models
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

# Create your views here.
class SearchView(ListView):
    template_name = 'pastebin_app/search.html'
    model = models.Post

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = models.Post.objects.filter(name__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)


class PostDetailView(DetailView):
    context_object_name = "post_detail"
    model = models.Post
    template_name = 'pastebin_app/detail.html'

class PostCreateView(CreateView):
    fields = ('name', 'content')
    model= models.Post

class PostUpdateView(UpdateView):
    fields = ('name','content')
    model = models.Post

class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy("pastebin_app:root")
