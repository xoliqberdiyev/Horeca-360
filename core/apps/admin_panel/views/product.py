from django.shortcuts import get_object_or_404 

from rest_framework import generics, views, status, parsers, filters
from rest_framework.permissions import IsAdminUser

from core.apps.admin_panel.serializers import product as serializers
from core.apps.shared.mixins.response import ResponseMixin
from core.apps.products.models import Product


class ProductListApiView(generics.GenericAPIView):
    serializer_class = serializers.AdminProductListSerializer
    queryset = Product.objects.select_related('category', 'unity').order_by('name')
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        page = self.paginate_queryset(self.filter_queryset(self.queryset))
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
    

class ProductCreateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(
                message='mahsulot qoshildi', status_code=status.HTTP_201_CREATED
            )
        return self.failure_response(message='mahsulot qoshishda hatolik', data=serializer.errors)
    

class ProductDeleteApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = None
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return self.success_response(
            message='product deleted', status_code=status.HTTP_204_NO_CONTENT
        )


class ProductUpdateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def patch(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = self.serializer_class(data=request.data, instance=product, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(
                message='mahsulot tahrirlandi',
            )
        return self.failure_response(message='mahsulot tahrirlashda hatolik', data=serializer.errors)
    
class ProductDetailApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = self.serializer_class(product)
        return self.success_response(message='product malumotlari', data=serializer.data)
    