from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from .models import User
import requests
import os

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
    
@api_view(['POST'])
def authenticate_code(request):
    if 'code' not in request.data.keys():
        return Response(data={'success': False, 'details': 'Authentication code was not provided'})
    
    code = request.data['code']
    client_id = os.getenv('GOOGLE_AUTH_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_AUTH_SECRET')
    frontend_url = os.getenv('FRONTEND_URL')
    
    url = "https://oauth2.googleapis.com/token?client_id=" + str(client_id)
    url += "&client_secret=" + str(client_secret)
    url += "&code=" + str(code)
    url += "&grant_type=authorization_code&redirect_uri=" + str(frontend_url)
    
    r = requests.post(url)
    print(url)
    print(r.text)
    
    return Response(data={'success': True})