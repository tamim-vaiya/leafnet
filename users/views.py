from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                login(request, user)
                return render(request, 'users/login_success.html')
            else:
                return HttpResponse("Invalid User!")

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
