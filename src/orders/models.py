from mongoengine import Document,fields,EmbeddedDocument
# Create your models here.
from src.products.models import Product
class Order(Document):
    user_id = fields.StringField(required=True)
    Address_id = fields.StringField(required=True)
    items = fields.ListField(fields.ReferenceFields(Product))
    total_amount = fields.DecimalField(required=True)
    taxes = fields.DecimalField(required=True)
    total_order_amount = fields.DecimalField(required=True)