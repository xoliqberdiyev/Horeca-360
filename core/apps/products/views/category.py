from rest_framework import generics, permissions
from rest_framework.response import Response

from core.apps.products.models import Category
from core.apps.products.serializers import category as serializers


class CategoryListApiView(generics.GenericAPIView):
    serializer_class = serializers.CategoryListSerializer
    queryset = Category.objects.all()
    permission_classes = []

    def get(self, request):
        category = self.get_queryset()
        page = self.paginate_queryset(category)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(category, many=True)
        return Response(serializer.data, status=200)
    

    