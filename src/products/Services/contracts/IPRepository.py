from abc import abstractmethod,ABC
from typing import List,Dict

from src.products.models import Product

class IProductRepository(ABC):  
    
          
    @abstractmethod        
    def create_product(self,data) -> Dict:
        return NotImplementedError
    @abstractmethod
    def get_object_by_id(self,id:int) -> Product:
        return NotImplementedError

    @abstractmethod
    def update_product(self,instance,data)-> Dict:
        return NotImplementedError

    @abstractmethod     
    def delete_product(self,product_id:int) -> bool:
        return NotImplementedError

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        return NotImplementedError
