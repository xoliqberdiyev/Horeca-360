from django.urls import path, include

from core.apps.admin_panel.views import user as user_views
from core.apps.admin_panel.views import banner as banner_views
from core.apps.admin_panel.views import unity as unity_views

urlpatterns = [
    path('user/', include(
        [
            path('create/', user_views.UserCreateApiView.as_view()),
            path('list/', user_views.UserListApiView.as_view()),
            path('<uuid:id>/update/', user_views.UserUpdateApiView.as_view()),
            path('<uuid:id>/delete/', user_views.UserDeleteApiView.as_view()),
            path('<uuid:id>/', user_views.UserDetailApiView.as_view()),
        ]
    )), 
    path('banner/', include(
        [
            path('create/', banner_views.BannerCreateApiView.as_view()),
            path('list/', banner_views.BannerListApiView.as_view()),
            path('<uuid:id>/', banner_views.BannerDetailApiView.as_view()),
            path('<uuid:id>/update/', banner_views.BannerUpdateApiView.as_view()),
            path('<uuid:id>/delete/', banner_views.BannerDeleteApiView.as_view()),
        ]
    )),
    path('unity/', include(
        [
            path('create/', unity_views.UnityCreateApiView.as_view()),
            path('list/', unity_views.UnityListApiView.as_view()),
            path('<uuid:id>/', unity_views.UnityDetailApiView.as_view()),
            path('<uuid:id>/update/', unity_views.UnityUpdateApiView.as_view()),
            path('<uuid:id>/delete/', unity_views.UnityDeleteApiView.as_view()),
        ]
    )),
]