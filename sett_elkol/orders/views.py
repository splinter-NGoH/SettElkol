from rest_framework import generics
from .models import OrderDetails, OrderItems
# from .serializers import OrderSerializer
from rest_framework import filters, generics, permissions, status
from rest_framework.response import Response
from .serializers import OrderCreateSerializer, OrderListSerializer

class OrderCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["chef_user"] = user.pkid
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = OrderDetails.objects.all()
    # renderer_classes = (MealsJSONRenderer,)
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = MealFilter
    ordering_fields = ["created_at"]

# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# from rest_framework import generics, mixins, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from orders.models import Order
# from orders.serializers import OrderSerializer
# from carty.models import CartItem

# class OrderList(generics.ListCreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         items = serializer.validated_data.get('items')
#         if not items:
#             return Response({'error': 'Cannot create an order without items.'}, status=status.HTTP_400_BAD_REQUEST)
#         total = sum(item.quantity * item.price for item in items)
#         serializer.save(user=self.request.user, total=total)

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.items.update(status='incart')
#         return super().destroy(request, *args, **kwargs)









# # from django.shortcuts import render
# # from .serializers import  OrderSerializer , CartItemSerializer
# # from .models import Order_Details , CartItem
# # from rest_framework import viewsets , generics, mixins, status ,filters
# # from rest_framework.views import APIView
# # from rest_framework.response import Response 
# # from django.http.response import JsonResponse
 
# # # POST
# # class AddToCartItem(APIView):
# #     def post(self,request):
# #         if CartItem.status == incart:
# #             return Response('cart item is already exist')
# #         else:
# #             CartItem.quantaties += 1
# #             serializer = MovieSerializer(data = request.data)
        
# #         # if serializer.is_valid():
# #         #     serializer.save()
# #         #     return Response(serializer.data , status= status.HTTP_201_CREATED)
# #         # return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)
    
    
# #     cartitem = Guist.objects.all()
# #     serializer = GuistSerializer(guist, many =True)
    










# # class Order_viewset(viewsets.ModelViewSet):
# #     queryset = Order_Details.objects.all()
# #     serializer_class = OrderSerializer
    


