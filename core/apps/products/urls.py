from django.urls import path, include

from core.apps.products.views import category as category_veiws
from core.apps.products.views import product as product_views
from core.apps.products.views import search as search_views

urlpatterns = [
    path('category/', include(
        [
            path('list/', category_veiws.CategoryListApiView.as_view()),
        ]
    )),
    path('product/', include(
        [
            path('<uuid:category_id>/list/', product_views.ProductListApiView.as_view()),
        ]
    )),
    path('search/', search_views.SearchApiView.as_view()),
]