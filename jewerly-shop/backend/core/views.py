from django.shortcuts import redirect, render
from django.contrib.auth import logout
from social_django.models import Code
from django.http import JsonResponse
import os


def my_view(request):
    return render(request, 'index.html')

def out(request):
    logout(request)
    return redirect('/')

def signInWithGoogle(request):
    frontend_url = os.getenv('FRONTEND_URL')
    client_id = os.getenv('GOOGLE_AUTH_CLIENT_ID')
    return redirect('https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=' + frontend_url + '&client_id=' + client_id + '&response_type=code&prompt=consent&scope=profile email')

def frontend(request):
    print(request.user)
    print(Code.objects.all())
    
    return JsonResponse(data={'success':True})
    
def read_request(request):
    print(request)
    return JsonResponse({'success': True})
    