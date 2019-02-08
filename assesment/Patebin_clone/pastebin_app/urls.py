from django.conf.urls import url
from . import views
from .views import PostCreateView, PostCreateView, PostUpdateView, PostDeleteView,SearchView

app_name = 'pastebin_app'
urlpatterns = [
    url(r'^search/$', views.SearchView.as_view(), name = 'search'),
    url(r'^$', views.PostCreateView.as_view(), name = 'root'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.PostDetailView.as_view(),name='detail'),
    url(r'^update/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.PostUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.PostDeleteView.as_view(),name='delete'),
]
