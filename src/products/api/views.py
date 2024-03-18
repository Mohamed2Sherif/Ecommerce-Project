from django.http import JsonResponse
from django.views import View
from src.products.Services.contracts.IPService import IProductService
class ProductsList(View):
    product_Service : IProductService
    def __init__(self,productService:IProductService):
        self.product_Service = productService
        
    def get(self,request,*args,**kwargs):
        products = self.product_Service.getAllProductsService.delay()
        return JsonResponse(products)
    
    
# Async function-based view for creating a new product (POST)
# def create_product(request):
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             create_product_async.delay(**serializer.validated_data)
#             cache.delete('product_list')  # Invalidate product list cache
#             return JsonResponse({'message': 'Product creation task has been scheduled'}, status=202)
#         return JsonResponse(serializer.errors, status=400)

# # Async function-based view for retrieving, updating, and deleting a product by ID (GET, PUT, DELETE)
# def product_detail(request, product_id):
#     if request.method == 'GET':
#         product = cache.get(f'product_{product_id}')
#         if not product:
#             product =  Product.objects.filter(id=product_id).first()
#             serializer = ProductSerializer(product)
#             cache.set(f'product_{product_id}', serializer.data)
#         return JsonResponse({'product': serializer.data})

#     elif request.method == 'PUT':
#         data =  request.json()
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid():
#             update_product_async.delay(product_id, **serializer.validated_data)
#             cache.delete(f'product_{product_id}')  # Invalidate product cache
#             cache.delete('product_list')  # Invalidate product list cache
#             return JsonResponse({'message': 'Product update task has been scheduled'}, status=202)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         delete_product_async.delay(product_id)
#         cache.delete(f'product_{product_id}')  # Invalidate product cache
#         cache.delete('product_list')  # Invalidate product list cache
#         return JsonResponse({'message': 'Product deletion task has been scheduled'}, status=202)
