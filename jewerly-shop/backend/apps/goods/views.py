from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Good
from .serializers import GoodSerializer
from rest_framework import status



class GoodViewSet(ModelViewSet):
    """
    Just anything that can be sold in jewerly shop
    """
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    def list(self, request, format=None):
        snippets = Good.objects.all()
        serializer = GoodSerializer(snippets, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
