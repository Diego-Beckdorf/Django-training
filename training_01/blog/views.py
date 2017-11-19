from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('blog:index')


@login_required
def index(request):
    return HttpResponse('Blog, Index')

@login_required
def new_post(request):
    return HttpResponse('Blog new post')


@login_required
def post(request):
    return HttpResponse('Blog  post')

@login_required
def my_posts(request):
    return HttpResponse('Blog my posts')
