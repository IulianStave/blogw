# blog.apps.BlogConfig should be added to project apps.py, within INSTALLED_APPS
from django.shortcuts import render

posts = [
    {
        'author': 'Stave',
        'title': 'Blog post',
        'content':'First post conent',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'John',
        'title': 'Blog post two',
        'content':'Second post conent',
        'date_posted': 'August 27, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About page'})


