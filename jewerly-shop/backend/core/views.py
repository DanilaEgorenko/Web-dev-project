from django.shortcuts import redirect, render
from django.contrib.auth import logout

def my_view(request):
    return render(request, 'index.html')

def out(request):
    logout(request)
    return redirect('/')