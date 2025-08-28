from rest_framework import views
from rest_framework.response import Response

from core.apps.products.models import Product, Category
from core.apps.products.serializers.category import CategoryListSerializer
from core.apps.products.serializers.product import ProductListSerializer


class SearchApiView(views.APIView):
    permission_classes = []

    def get(self, request):
        search = request.query_param.get('search')
        if search is None:
            return Response({"success": False, "message": 'search is required'}, status=400)
        products = Product.objects.filter(name__istartswith=search)
        categories = Category.objects.filter(name__istartswith=search)
        
        return Response(
            {
                'products': ProductListSerializer(products, many=True).data,
                'categories': CategoryListSerializer(categories, many=True).data,
            },
            status=200
        )

