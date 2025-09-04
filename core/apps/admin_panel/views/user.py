from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status, views
from rest_framework_simplejwt.tokens import RefreshToken

from core.apps.admin_panel.serializers.user import UserSerializer, UserLoginSerializer
from core.apps.accounts.models import User
from core.apps.shared.mixins.response import ResponseMixin


class UserCreateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(
                message='User qoshildi', status_code=status.HTTP_201_CREATED
            )
        return self.error_response(data=serializer.errors, message='User qoshishda xatolik')
    

class UserListApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        users = self.get_queryset()
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(users, many=True)
        return self.success_response(data=serializer.data, message='userlar royxati')
    

class UserUpdateApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.success_response(message='user tahrirlandi')
        return self.failure_response(data=serializer.errors, message='user tahrirlashda xatolik')


class UserDeleteApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = None
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return self.success_response(message='user ochirildi', status_code=status.HTTP_204_NO_CONTENT)


class UserDetailApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permissions = [permissions.IsAdminUser]

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = self.serializer_class(user)
        return self.success_response(data=serializer.data, message='user malumotlari')


class UserDashboardApiView(views.APIView, ResponseMixin):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        admin_users = User.objects.filter(is_superuser=True).count()
        users = User.objects.filter(is_superuser=False).count()
        return self.success_response(
            data={'admin_users': admin_users, 'users': users},
            message='userlar soni',
        )
    

class UserLoginApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            token = RefreshToken.for_user(user)
            return self.success_response(
                data={
                    'access': str(token.access_token),
                    'refresh': str(token)
                },
                message='user tizimga kirish muvaffaqiyatli yakunlandi'
            )
        return self.failure_response(message='user tizimga kirishda xatolik', data=serializer.errors)