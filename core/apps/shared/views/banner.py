from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.apps.shared.models import Banner
from core.apps.shared.serializers import banner as serializers


class BannerListApiView(GenericAPIView):
    serializer_class = serializers.BannerListSerializer
    queryset = Banner.objects.all()
    pagination_class = None
    
    def get(self, request):
        banners = Banner.objects.all()
        serializer = self.serializer_class(banners, many=True)
        return Response(serializer.data, status=200)
    