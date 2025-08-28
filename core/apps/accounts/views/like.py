from django.shortcuts import get_object_or_404

from rest_framework import views, permissions, generics
from rest_framework.response import Response

from core.apps.accounts.models import Like
from core.apps.products.models import Product
from core.apps.products.serializers.product import ProductListSerializer


class LikeApiView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        like, created = Like.objects.get_or_create(product=product, user=request.user)
        if created:
            return Response({'success': True, 'message': "Liked"}, status=200)
        like.delete()
        return Response({'success': False, 'message': "Unliked"}, status=200)


class LikeProductListApiView(generics.GenericAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.filter(likes__user=request.user)
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.serializer_class(page, many=True, context={'user': request.user})
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(products, many=True, context={'user': request.user})
        return Response(serializer.data, status=200)
