from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
    
@api_view(['POST'])
def authenticate_code(request):
    if 'code' not in request.data.keys():
        return Response(data={'success': False, 'details': 'Authentication code was not provided'})
    
    code = request.data['code']
        
    
    
    return Response(data={'success': True})