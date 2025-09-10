from django.shortcuts import get_object_or_404

from rest_framework import generics, views, status
from rest_framework.permissions import IsAdminUser

from core.apps.shared.mixins.response import ResponseMixin
from core.apps.admin_panel.serializers.order import OrderSerializer
from core.apps.orders.models import Order


class OrderListApiView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.select_related('user').prefetch_related('items', 'items__product').order_by('order_number')
    permission_classes = [IsAdminUser]

    def get(self, request):
        date = request.query_params.get('date')
        name = request.query_params.get('name')
        if date:
            self.queryset = self.queryset.filter(date=date)
        if name:
            self.queryset = self.queryset.filter(name=name)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)


class OrderDeleteApiView(views.APIView, ResponseMixin):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order.delete()
        return self.success_response(status_code=status.HTTP_204_NO_CONTENT)