from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status, parsers

from core.apps.shared.models import Banner
from core.apps.shared.mixins.response import ResponseMixin
from core.apps.admin_panel.serializers.banner import BannerSerializer


class BannerCreateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(message='banner qoshildi', status_code=status.HTTP_201_CREATED)
        return self.failure_response(data=serializer.errors, message='banner qoshishda hatolik')


class BannerUpdateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def patch(self, request, id):
        banner = get_object_or_404(Banner, id=id)
        serializer = self.serializer_class(data=request.data, instance=banner)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(message='banner tahrirlandi')
        return self.failure_response(message='banner tahrirlashda hatolik', data=serializer.errors)


class BannerDeleteApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, id):
        banner = get_object_or_404(Banner, id=id)
        banner.delete()
        return self.success_response(message='banner ochirildi', status_code=status.HTTP_204_NO_CONTENT)
    

class BannerDetailApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id):
        banner = get_object_or_404(Banner, id=id)
        serializer = self.serializer_class(banner)
        return self.success_response(message='banner malumotlari', data=serializer.data)
    

class BannerListApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        banners = self.queryset
        page = self.paginate_queryset(banners)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        
