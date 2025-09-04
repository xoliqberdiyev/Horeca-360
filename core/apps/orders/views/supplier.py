from rest_framework import views, permissions, generics
from rest_framework.response import Response

from core.apps.orders.models import Supplier
from core.apps.orders.serializers.supplier import SupplierListSerializer


class SupplierCreateApiView(views.APIView):
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        full_name = data.get('full_name')
        tg_id = data.get('tg_id')
        Supplier.objects.create(
            phone=phone,
            full_name=full_name,
            tg_id=tg_id
        )
        return Response({'success': True, 'message': 'created'}, status=200)


class SupplierListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Supplier.objects.all()
    serializer_class = SupplierListSerializer
    pagination_class = None


class SupplierGetApiView(views.APIView):
    def get(self, request, tg_id):
        supp = Supplier.objects.filter(tg_id=tg_id).first()
        if supp:
            return Response({'success': True}, status=200) 
        else:
            return Response({"success": False},status=404)