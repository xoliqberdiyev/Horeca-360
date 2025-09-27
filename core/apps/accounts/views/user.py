from rest_framework import generics, views
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers.user import CustomUserLoginSerializer, UserListSerializer
from core.apps.accounts.models import User


class UserLoginApiView(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)})
        return Response(data=serializer.errors)


class UserListApiView(views.APIView):
    def get(self, request):
        users = User.objects.exclude(tg_id__isnull=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=200)
    