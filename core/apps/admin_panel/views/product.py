from rest_framework import generics, views
from rest_framework.permissions import IsAdminUser

from core.apps.admin_panel.serializers import product as serializers
from core.apps.shared.mixins.response import ResponseMixin
from core.apps.products.models import Product


class ProductListApiView(generics.GenericAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = Product.objects.select_related('category', 'unity')
    permission_classes = [IsAdminUser]

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
    

# class ProductCreateApiView(generics.GenericAPIView, ResponseMixin):


