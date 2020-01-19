from rest_framework import serializers
from iot.models import Device, UserInterface, RaspberryGpio

class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    shell_in = serializers.SerializerMethodField(read_only=True)
    shell_out = serializers.SerializerMethodField(read_only=True)
    telegram = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Device
        fields = "__all__"

    def get_shell_in(self, obj):
        return f"devices/{obj.id}/shell/in"

    def get_shell_out(self, obj):
        return f"devices/{obj.id}/shell/out"

    def get_telegram(self, obj):
        return f"devices/{obj.id}/telegram"

class UserInterfaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInterface
        fields = "__all__"
        extra_kwargs = {'device': {'read_only': True}}

class RaspberryGpioSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaspberryGpio
        fields = "__all__"
        extra_kwargs = {'device': {'read_only': True}}