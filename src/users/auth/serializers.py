from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomVerifyEmailSerializer(serializers.Serializer):
    otp = serializers.CharField(write_only=True)


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }
