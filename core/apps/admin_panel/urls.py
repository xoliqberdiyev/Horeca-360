from django.urls import path, include

from core.apps.admin_panel.views import user as user_views

urlpatterns = [
    path('user/', include(
        [
            path('create/', user_views.UserCreateApiView.as_view()),
            path('list/', user_views.UserListApiView.as_view()),
            path('<uuid:id>/update/', user_views.UserUpdateApiView.as_view()),
            path('<uuid:id>/delete/', user_views.UserDeleteApiView.as_view()),
            path('<uuid:id>/', user_views.UserDetailApiView.as_view()),
        ]
    ))
]