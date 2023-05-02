# from rest_framework import serializers
# from shipment.models import Shipment
# from carty.serializers import CartItemSerializer

# class ShipmentSerializer(serializers.ModelSerializer):
#     cart_items = CartItemSerializer(many=True)

#     class Meta:
#         model = Shipment
#         fields = ['id', 'cart_items', 'user', 'address', 'city', 'status', 'created_at']