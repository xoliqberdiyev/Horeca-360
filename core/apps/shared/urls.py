from django.urls import path, include

from core.apps.shared.views.banner import BannerListApiView


urlpatterns = [
    path('banner/list/', BannerListApiView.as_view()),
]