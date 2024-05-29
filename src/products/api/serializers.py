from rest_framework import serializers
from src.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
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
