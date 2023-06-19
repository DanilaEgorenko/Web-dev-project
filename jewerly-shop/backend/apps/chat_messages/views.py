from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializers import ChatSerializer
from .models import Message, Chat
from apps.users.models import User

class ChatViewSet(ModelViewSet):
    """
    Yeah, it is messages viewset :/
    """
    serializer_class = ChatSerializer
    queryset = Message.objects.all()

    def list(self, request, format=None):
        user = request.user
        print(user)
        if user.is_anonymous:
            return Response(data={'error': 'you are not logged in'})
        
        messages = Message.objects.filter(user=user)
        chat_ids = []
        
        for message in messages:
            if message.chat_id not in []:
                chat_ids.append(message.chat_id)
                
        return Response(data=chat_ids)
    

    # def retrive(self, request, format=None):
    #     chat_id = request.chat_id
    #     queryset = Message.objects.filter(chat_id=chat_id)
    #     serializer = ChatSerializer(queryset, many=True)
        
    #     return Response(serializer.data)

    def create(self, request, format=None):
        user = request.user
        
        if user.is_anonymous:
            return Response(data={'error': 'you are not logged in'})
        
        recipient_email = request.data.get('email')
        message_text = request.data.get('text')
        recipient = User.objects.filter(email=recipient_email).first()
        
        if not recipient:
            return Response(data={'error': 'user with email ' + recipient_email + ' was not found'})
        
        if not message_text:
            return Response(data={'error': 'it seems you\'ve sent an empty message'})

        chat = Chat.objects.filter(user1=user, user2=recipient) or Chat.objects.filter(user1=recipient, user2=user)
        if len(chat) > 0:
            chat = chat.last()
        else:
            chat = Chat.objects.create(user1=user, user2=recipient)

        Message.objects.create(chat=chat, text=message_text, user=user)
        
        return Response(data={'success': True})