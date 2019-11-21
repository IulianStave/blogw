# blog.apps.BlogConfig should be added to project apps.py, within INSTALLED_APPS
from django.shortcuts import render

posts = [
    {
        'author': 'Iulian Stave',
        'title': 'First blog post',
        'content':'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'John Smith',
        'title': 'Second post',
        'content':'Second post content',
        'date_posted': 'August 3, 2019'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Blog start',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About page'})


