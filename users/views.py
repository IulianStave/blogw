from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# there are many types of messages from the messages librarary  
# messages.debug .info .success .warning .error

# Create your views here.
# use the same folder structure to store the register.html users/templates/users/register.html

def register(request):
    # we instatiate a form with that data (request.POST) in case of POST request
    # otherwise, instantiate a blank form if we don't a get a POST request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created, please log in!')
            return redirect('login') 
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
