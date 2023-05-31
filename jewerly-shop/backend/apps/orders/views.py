from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Order
from .serializers import OrderSerializer, GetOrderSerializer, CTASerrializer
from django.core.mail import send_mail


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, format=None):
        snippets = Order.objects.all()
        serializer = OrderSerializer(data=snippets, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        data = Order.objects.all()
        serializer = GetOrderSerializer(data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CTAViewSet(ModelViewSet):
    queryset = None
    serializer_class = CTASerrializer

    def list(self, request):
        return Response(data={'error':'get is not allowed'})
    
    def create(self, request):
        email = request.data['email']
        name = request.data['name']
        try:
            send_mail('CTA on your website!', 'Your client ' + name + ' with email ' + email + ' asks about contact!', from_email="1@mail.ru", recipient_list=["2@mail.ru"])
            return Response(data={'success':'true'})
        except Exception:
            return Response(data={'success':'false'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        