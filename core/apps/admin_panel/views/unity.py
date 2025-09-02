from django.shortcuts import get_object_or_404

from rest_framework import generics, status, permissions

from core.apps.products.models import Unity
from core.apps.admin_panel.serializers.unity import UnitySerializer
from core.apps.shared.mixins.response import ResponseMixin


class UnityCreateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UnitySerializer
    queryset = Unity.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(message='birlik qoshildi', status_code=status.HTTP_201_CREATED)
        return self.failure_response(message='birlik qoshishda xatolik', data=serializer.errors)
    

class UnityListApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UnitySerializer
    queryset = Unity.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        queryset = self.queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
    

class UnityDeleteApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UnitySerializer
    queryset = Unity.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, id):
        unity = get_object_or_404(Unity, id=id)
        unity.delete()
        return self.success_response(message='birlik ochirildi', status_code=status.HTTP_204_NO_CONTENT)
    

class UnityUpdateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UnitySerializer
    queryset = Unity.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, id):
        unity = get_object_or_404(Unity, id=id)
        serializer = self.serializer_class(data=request.data, instance=unity)
        if serializer.is_valid():
            serializer.save()
            return self.success_response(message='birlik tahrirlandi')
        return self.failure_response(message='hatolik', data=serializer.errors)


class UnityDetailApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UnitySerializer
    queryset = Unity.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id):
        unity = get_object_or_404(Unity, id=id)
        serializer = self.serializer_class(unity)
        return self.success_response(message='birlik malumotlari', data=serializer.data)
