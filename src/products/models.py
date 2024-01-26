from mongoengine import Document, fields, EmbeddedDocument

class Specification(EmbeddedDocument):
    size = fields.StringField()
    color = fields.StringField()
    images = fields.ListField(fields.URLField())

# Define the main Product document
class Product(Document):
    #TODO: when adding the product add the ID
    #and rename it to product_id
    name = fields.StringField(required=True)
    price = fields.DecimalField(required=True)
    specifications = fields.EmbeddedDocumentField(Specification)
    vendor_id = fields.StringField(required=True)  # Use ReferenceField

    # Additional field for category-specific data for each new category in the website
    category_specific_field = fields.DictField()
    meta = {
        "strict": False,
        "allow_inheritance": True,
        "indexes": [{"fields": ["name", "price", "category_specific_field"]}],
        "collection": "Products",
    }
