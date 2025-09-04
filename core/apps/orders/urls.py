from django.urls import path, include

from core.apps.orders.views import order as order_views
from core.apps.orders.views import supplier as supp_views

urlpatterns = [
    path('order/create/', order_views.OrderCreateApiView.as_view()),
    path('order/list/', order_views.OrderListApiView.as_view()),
    path('supplier/create/', supp_views.SupplierCreateApiView.as_view()),
    path('supplier/<str:tg_id>/', supp_views.SupplierGetApiView.as_view()),
    path('supplier/list/', supp_views.SupplierListApiView.as_view()),
]