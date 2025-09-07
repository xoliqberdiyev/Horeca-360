from django.shortcuts import get_object_or_404

from rest_framework import generics, views, filters
from rest_framework.response import Response

from core.apps.products.models import Product, Category
from core.apps.products.serializers import product as serializers


class ProductListApiView(generics.GenericAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = Product.objects.select_related('unity')
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category).select_related('unity')
        page = self.paginate_queryset(self.filter_queryset(products))
        if page is not None:
            serializer = self.serializer_class(page, many=True, context={'user': request.user})
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(products, many=True, context={'user': request.user})
        return Response(serializer.data, status=200)


class ProductsApiView(generics.GenericAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = Product.objects.select_related('unity')
    permission_classes = []

    def get(self, request):
        products = self.queryset
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=200)
    

class ProductDetailApiView(generics.GenericAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = Product.objects.select_related('unity')
    permission_classes = []

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=200)
    

class UpdateProductTgIdApiView(views.APIView):
    def post(self, request, product_code):
        product = get_object_or_404(Product, code=product_code)
        product.tg_id = request.data.get('tg_id')
        product.save()
        return Response({'success': True, 'message': 'telegram id saqlandi'}, status=200)