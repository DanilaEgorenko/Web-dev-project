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
    queryset = Chat.objects.all()

    def list(self, request, format=None):
        user = request.user
        
        if user.is_anonymous:
            return Response(data={'error': 'you are not logged in'})
        
        chats = Chat.objects.filter(user1=user)
        chats2 = Chat.objects.filter(user2=user)
        chat_ids = {}
        
        for chat in chats:
            if chat.id not in []:
                chat_ids[str(len(chat_ids))] = { 'id': chat.id, 'user': chat.user2.username }
                
        for chat in chats2:
            if chat.id not in []:
                chat_ids[str(len(chat_ids))] = { 'id': chat.id, 'user': chat.user1.username }
        
        return Response(data=chat_ids)
    

    def retrieve(self, request,  *args, **kwargs):
        user = request.user
        
        if user.is_anonymous:
            return Response(data={'error': 'you are not logged in'})
        
        instance = self.get_object()
        recipient = instance.user1
        
        if user == recipient:
            recipient = instance.user2
        
        recipient_name = recipient.username
        recipient_email = recipient.email
        
        return Response(data={'recipient_name': recipient_name, 'recipient_email': recipient_email })

    @action(methods=['GET'], detail=True)
    def messages(self, request,  *args, **kwargs):
        user = request.user
        
        if user.is_anonymous:
            return Response(data={'error': 'you are not logged in'})
        
        instance = self.get_object()
        
        messages_queryset = Message.objects.filter(chat=instance).order_by('created_at')
        messages = []
        
        for message in messages_queryset:
            if message.user == user:
                messages.append({'user': 'you', 'text': message.text})
            else:
                messages.append({'user': message.user.username, 'text': message.text})    
            
            
        
        return Response(data=messages)

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
        
        if user == recipient:
            return Response(data={'error': 'you can\'t send message to yourself'})

        chat = Chat.objects.filter(user1=user, user2=recipient) or Chat.objects.filter(user1=recipient, user2=user)
        if len(chat) > 0:
            chat = chat.last()
        else:
            chat = Chat.objects.create(user1=user, user2=recipient)

        Message.objects.create(chat=chat, text=message_text, user=user)
        
        return Response(data={'success': True, 'chat_id': chat.id})