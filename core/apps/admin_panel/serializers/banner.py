from rest_framework import serializers

from core.apps.shared.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id', 'banner'
        ]
        