# blog.apps.BlogConfig should be added to project apps.py, within INSTALLED_APPS
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog start',
    }
    return render(request, 'blog/home.html', context)

#class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model>_<viewtype>.html = > blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # show the newest first

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title':'About page'})


