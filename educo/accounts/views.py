from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import login, authenticate

def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
