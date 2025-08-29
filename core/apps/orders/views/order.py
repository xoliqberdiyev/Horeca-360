from rest_framework import generics, permissions
from rest_framework.response import Response

from core.apps.orders.models import Order, OrderItem
from core.apps.orders.serializers import order as serializers


class OrderCreateApiView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {'success': True, 'message': 'Firdavs aka order create qilindi, tekshirib koring'},
                status=200
            )
        return Response(
            {
                'success': False,
                "message": "Firdavs aka order create qilishda xatolik chiqdi, errorni oqib koring",
                'error': serializer.errors,
            },
            status=400
        )