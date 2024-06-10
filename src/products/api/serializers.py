from rest_framework import serializers
from src.products.models import Product
from src.orders.utils import SizeChoices


class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.ListField(
        child=serializers.MultipleChoiceField(choices=SizeChoices.CHOICES)
    )

    class Meta:
        model = Product
        fields = ["id", "product_info", "category_info"]
        read_only_fields = ["created_time", "id", "updated_time"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["sizes"] = instance.sizes.split(",")
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        sizes = data.get("sizes", [])
        internal_value["sizes"] = ",".join(sizes)
        return internal_value
