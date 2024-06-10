from rest_framework import serializers
from src.products.models import Product
from src.orders.utils import SizeChoices


class CommaSeparatedField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop("choices", None)
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        if value is None:
            return []
        return value.split(",")

    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError("Expected a list of items")
        if not data:
            raise serializers.ValidationError("this field cannot be empty")
        if self.choices:
            for item in data:
                if item not in dict(self.choices):
                    raise serializers.ValidationError("Invalid Choice:{item}")
            return ",".join(data)


class ProductSerializer(serializers.ModelSerializer):
    available_sizes = CommaSeparatedField(choices=SizeChoices.CHOICES)
    available_colors = CommaSeparatedField(choices=SizeChoices.CHOICES)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["created_time", "id", "updated_time"]
