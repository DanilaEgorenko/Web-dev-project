from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from .models import User, GoogleAuthTokens as Oauth
import requests
import os

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

@api_view(['GET'])
def get_user(request):
    user = request.user
    
    token = Oauth.objects.filter(user=user).last()
    if token:
        access_token = token.access_token

        profile_api_url = "https://www.googleapis.com/userinfo/v2/me"
        headers = {
            "Authorization": "Bearer " + access_token
        }
        
        response = requests.get(profile_api_url, headers=headers)
        data = response.json()
        picture = data.get('picture')
    
    else:
        picture = 'somepicture'
    
    email = user.email
    username = user.username
    return Response(data={
        "email": email,
        "username": username,
        "picture": picture
    })
    

@api_view(['POST'])
def authenticate_code(request):
    if 'code' not in request.data:
        return Response(data={'success': False, 'details': 'Authentication code was not provided'})
    
    code = request.data['code']
    client_id = os.getenv('GOOGLE_AUTH_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_AUTH_SECRET')
    frontend_url = os.getenv('FRONTEND_URL')
    
    url = "https://oauth2.googleapis.com/token"
    request_json_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": frontend_url
    }
    
    # Обмениваем auth_code на access_token
    response = requests.post(url, json=request_json_data)
    data = response.json()
    if 'error' in data:
        return Response(data=data)
    
    access_token = data.get('access_token')
    id_token = data.get('id_token')
    expires_in = data.get('expires_in')
    # token_type = data['token_type']
    # scope = data['scope'] тоже могут понадобиться в будущем
    
    profile_api_url = "https://www.googleapis.com/userinfo/v2/me"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    
    # Получаем информацию о профиле
    response = requests.get(profile_api_url, headers=headers)
    data = response.json()
    email = data.get('email')
    username = data.get('name')
    user = User.objects.filter(email=email).first()
    # Создаем пользователя, если его нет
    if not user:
        user = User.objects.create(email=email, username=username)
    
    Oauth.objects.create(access_token=access_token, id_token=id_token, expires_in=expires_in, user=user)
    
    return Response(data={'token': user.token})


@api_view(['GET'])
def check_jwt(request):
    user = request.user
    
    if user.is_anonymous:
        return Response(data={"error": "no jwt provided"})
    
    token = request.user.token
    return Response(data={"success": True ,"token": token})
    

class NotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return True
        
        return False


class LoginView(APIView):
    permission_classes = [NotAuthenticated]
    
    def post(self, request):
        email = request.data.get('email')
        # phone = request.data.get('phone')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        
        if not user:
            return Response(data = {'error': 'wrong email or password'})

        if user.check_password(password):
            print('ok')
            
        return Response(data={'success': True, 'token': user.token})