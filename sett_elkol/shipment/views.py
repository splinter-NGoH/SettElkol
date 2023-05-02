# from rest_framework import generics, mixins, viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Shipment
# from .serializers import ShipmentSerializer

# class ShipmentViewSet(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       viewsets.GenericViewSet):
#     queryset = Shipment.objects.all()
#     serializer_class = ShipmentSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Shipment.objects.filter(user=self.request.user)
