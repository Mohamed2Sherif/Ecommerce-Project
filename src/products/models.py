from mongoengine import Document,fields,EmbeddedDocument

class Specification(EmbeddedDocument):
    size = fields.StringField()
    color = fields.StringField()

# Define the main Product document
class Product(Document):
    name = fields.StringField(required=True)
    price = fields.DecimalField(required=True)
    specifications = fields.EmbeddedDocumentField(Specification)
    
    # Additional field for category-specific data for each new category in the website
    category_specific_field = fields.DictField()
    meta = {
        'strict': False,
        'allow_inheritance': True,
        'indexes': [
            {'fields':['name','price','category_specific_field']}
        ],
        'collection': 'Products',
    }