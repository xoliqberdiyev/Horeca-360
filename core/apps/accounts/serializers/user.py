from rest_framework import serializers

from core.apps.accounts.models import User


class CustomUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    tg_id = serializers.CharField(required=False)

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if not user:
            raise serializers.ValidationError("User not found")
        if data.get('tg_id'):
            user.tg_id = data.get('tg_id')
            user.save()
        data['user'] = user
        return data