from django.shortcuts import get_object_or_404

from rest_framework import generics, views, permissions, status

from core.apps.shared.mixins.response import ResponseMixin
from core.apps.products.models import Category
from core.apps.admin_panel.serializers.category import CategorySerializer


class CategoryListApiView(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
    

class CategoryCreateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(
                message='kategoriya qoshildi', status_code=status.HTTP_201_CREATED
            )
        return self.failure_response(message='kategoriya qoshishda hatolik', data=serializer.errors)


class CategoryDeleteApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = None
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return self.success_response(
            message='kategoriya ochirildi', status_code=status.HTTP_204_NO_CONTENT
        )


class CategoryUpdateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = self.serializer_class(data=request.data, instance=category)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(message='kategoriya tahrirlandi')
        return self.failure_response(data=serializer.errors, message='kategoriya tahrirlashda hatolik')


