# documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product
from .serializers import ProductSerializer

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    id = fields.IntegerField(attr='id')
    name = fields.TextField(attr='name')
    product_info = fields.ObjectField(attr='product_info')
    price = fields.FloatField(attr='price')

    class Django:
        model = Product
        serializer_class = ProductSerializer
