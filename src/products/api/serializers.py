from adrf import serializers as async_serializers
from ..models import Product
from rest_framework import serializers


class ProductSerializer(async_serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    def validate_product_info(self, value):
        if "name" not in value:
            raise serializers.ValidationError(
                "Product_info must contain a name attribute"
            )
        if "price" not in value:
            raise serializers.ValidationError(
                "product information must contain a price attribute"
            )
        if "qty" not in value:
            raise serializers.ValidationError(
                "product information must contain a quantity attribute"
            )

        return value

    class Meta:
        model = Product
        fields = ["id", "product_info", "category_info"]
        read_only_fields = ["created_time", "id", "updated_time"]
