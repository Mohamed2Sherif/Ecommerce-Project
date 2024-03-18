from typing import Dict
from src.products.Services.contracts.IPRepository import IProductRepository
from src.products.Services.contracts.IPService import IProductService
from src.products.models import Product
from celery import shared_task

@shared_task
class ProductService(IProductService):
    def __init__(self,product_repository:IProductRepository):
        self.repository = product_repository
        
    def createProductService(self,request_data) -> Dict:
        return self.repository.create_product(data=request_data)
    
    def updateProductService(self,product_id,data) -> Dict:
        instance = self.repository.get_object_by_id(product_id)
        return self.repository.update_product(instance,data)
        
    def getProductService(self,product_id) -> Product:
        return self.repository.get_object_by_id(product_id)
        
    def deleteProductService(self,product_id):
        return True == self.repository.delete_product(product_id)
        
    def getAllProductsService(self):
        return self.repository.get_all_products()