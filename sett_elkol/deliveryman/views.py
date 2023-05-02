from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView 

# from authors_api.settings.production import DEFAULT_FROM_EMAIL

from .exceptions import  CantFollowYourself , NotYourDelivary 
from .models import Deliv
from .pagination import DelivaryPagination
from .renderers import  DelivaryJSONRenderer
from .serializers import  UpdateDelivarySerializer, DelivarySerializer

User = get_user_model() 

# DelivaryJSONRenderer
class DelivaryListAPIView(generics.ListAPIView):
    serializer_class = DelivarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Deliv.objects.all()
    renderer_classes = (DelivaryJSONRenderer,)
    pagination_class = DelivaryPagination


class DelivaryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Deliv.objects.select_related("user")
    serializer_class = DelivarySerializer
    renderer_classes = (DelivaryJSONRenderer,)

    def retrieve(self, request, username, *args, **kwargs):
        try:
            delivary = self.queryset.get(user__username=username)
        except Deliv.DoesNotExist:
            raise NotFound("A Delivary with this username does not exist")

        serializer = self.serializer_class(delivary, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class DelivaryProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Deliv.objects.select_related("user")
    serializer_class = DelivarySerializer
    renderer_classes = (DelivaryJSONRenderer,)

    def retrieve(self, request, *args, **kwargs):
        try:
            delivary = self.queryset.get(user=request.user)
        except Deliv.DoesNotExist:
            raise NotFound("A Delivary with this username does not exist")

        serializer = self.serializer_class(delivary, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateDelivaryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Deliv.objects.select_related("user")
    renderer_classes = [DelivaryJSONRenderer]
    serializer_class = UpdateDelivarySerializer

    def patch(self, request, username):
        try:
            self.queryset.get(user__username=username)
        except Deliv.DoesNotExist:
            raise NotFound("A Delivary with this username does not exist")

        user_name = request.user.username
        if user_name != username:
            raise NotYourDelivary

        data = request.data
        serializer = UpdateDelivarySerializer(
            instance=request.user.Deliv, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

