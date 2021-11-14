from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Articles

class ArticlesListView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'

class ArticlesUpdateView(UpdateView):
    model = Articles
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

class ArticlesDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url=reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo', 'author')




