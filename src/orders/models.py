from mongoengine import Document,fields,EmbeddedDocument
# Create your models here.
from src.products.models import Product

class Order(Document):
    user_id = fields.StringField(required=True)
    Address_id = fields.StringField(required=True)
    items = fields.ListField(fields.ReferenceField(Product))
    total_amount = fields.DecimalField(required=True)
    taxes = fields.DecimalField(required=True)
    total_order_amount = fields.DecimalField(required=True)
    vendor_id = fields.ListField(fields.StringField())
    
    meta ={
        "strict":False,
        "allow_inheritance":True,
        "indexes":[{"fields":["user_id","Address_id","total_order_amount",]}],
        "collection":"Orders",
        
    }