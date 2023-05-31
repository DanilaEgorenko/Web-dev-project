from django.shortcuts import get_object_or_404
import json
from .models import Reviews
from apps.goods.models import Good
from apps.users.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse

class ReviewCreateView(APIView):
    def post(self, request):
        user_data = json.loads(request.data.get('user_id'))
        text = request.data.get('text')
        product_data = json.loads(request.data.get('good_id'))
        date = request.data.get('date')
        rating = request.data.get('rating')

        product_id = product_data[0]['pk']
        user_id = user_data[0]['pk']

        product = Good.objects.get(pk=product_id)

        review = Reviews.objects.create(username_id=user_id, text=text, product=product, created_at=date, rate=rating)

        return Response({'message': 'Отзыв успешно создан'})

def get_good(request):
    good = get_object_or_404(Good, id=1)

    serialized_good = serializers.serialize('json', [good])

    return JsonResponse(serialized_good, safe=False)

def get_user(request):
    user = get_object_or_404(User, id=1)

    serialized_user = serializers.serialize('json', [user])

    return JsonResponse(serialized_user, safe=False)