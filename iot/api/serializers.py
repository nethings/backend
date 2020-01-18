from rest_framework import serializers
from iot.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    #topic = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Device
        fields = "__all__"