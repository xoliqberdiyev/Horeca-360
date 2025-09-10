from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView
from core.apps.accounts.views import like as like_views
from core.apps.accounts.views import user


urlpatterns = [
    path('login/', user.UserLoginApiView.as_view()),    
    path('<uuid:product_id>/like/', like_views.LikeApiView.as_view()),
    path('liked_products/', like_views.LikeProductListApiView.as_view()),
]