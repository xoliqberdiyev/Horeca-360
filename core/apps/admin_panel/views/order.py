from rest_framework import generics, views, status
from rest_framework.permissions import IsAdminUser

from core.apps.shared.mixins.response import ResponseMixin
from core.apps.admin_panel.serializers.order import OrderSerializer
from core.apps.orders.models import Order


class OrderListApiView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.select_related('user')
    permission_classes = [IsAdminUser]

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)