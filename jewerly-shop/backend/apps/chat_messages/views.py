from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .models import Message

class MessageViewSet(ModelViewSet):
    """
    Yeah, it is messages viewset :/
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def list(self, request, format=None):
        if request.GET['chat_id'] is None:
            data = {
                "details": "Chat Id is required"
            }
            return Response(data=data, status=status.HTTP_200_OK)
        
        chat_id = request.GET['chat_id']
        serializer = self.serializer_class
        queryset = Message.objects.filter(chat_id=chat_id)
        data = serializer(queryset, many=True).data
            
        return Response(data=data, status=status.HTTP_200_OK)

    def retrive(self, request, format=None):
        chat_id = request.chat_id
        queryset = Message.objects.filter(chat_id=chat_id)
        serializer = MessageSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)