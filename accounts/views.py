from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = authenticate(request, username=form.cleaned_data['username'],
            #                         password=form.cleaned_data['password1'],)
            # auth_login(request, user)
            user = form.cleaned_data.get('first_name')
            # get_username = form.cleaned_data.get('username')
            # x = User.objects.values('id').filter(username=get_username).first()
            # p=Profile(user_id=x['id'])
            # p.save()
            # bio_data = CreateUserBio.objects.filter(user=x['id'])
            messages.success(request,'congratulations ' + user + ' Your account is created you can login now!')
            return redirect('login')
    context = {'form': form, 'signupsucess': 'Congratulation you are logged in with successful signup process'}
    return render (request, 'signup1.html', context )

def login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           auth_login(request, user)
           return redirect('home')
       else:
           messages.info(request, 'Username or password are not correct')
    
    context = {}
    return render (request, 'login1.html', context)