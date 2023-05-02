from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import CartItem
# from .serializers import CartItemSerializer

# class CartItemList(generics.ListCreateAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)

# class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)


# from rest_framework import generics, mixins, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import CartItem
# from .serializers import CartItemSerializer

# class CartItemViewSet(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         item_name = serializer.validated_data.get('item_name')
#         if CartItem.objects.filter(user=self.request.user, item_name=item_name, status='incart').exists():
#             return Response({'error': 'This item is already in your cart.'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save(user=self.request.user)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)