from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from .tasks import create_product_async, update_product_async, delete_product_async
from django.core.cache import cache

# Async function-based view for listing all products (GET)
async def list_products(request):
    if request.method == 'GET':
        products = cache.get('product_list')
        if not products:
            products = await Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            cache.set('product_list', serializer.data)
        return JsonResponse({'products': serializer.data})

# Async function-based view for creating a new product (POST)
async def create_product(request):
    if request.method == 'POST':
        data = await request.json()
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            create_product_async.delay(**serializer.validated_data)
            cache.delete('product_list')  # Invalidate product list cache
            return JsonResponse({'message': 'Product creation task has been scheduled'}, status=202)
        return JsonResponse(serializer.errors, status=400)

# Async function-based view for retrieving, updating, and deleting a product by ID (GET, PUT, DELETE)
async def product_detail(request, product_id):
    if request.method == 'GET':
        product = cache.get(f'product_{product_id}')
        if not product:
            product = await Product.objects.filter(id=product_id).first()
            serializer = ProductSerializer(product)
            cache.set(f'product_{product_id}', serializer.data)
        return JsonResponse({'product': serializer.data})

    elif request.method == 'PUT':
        data = await request.json()
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            update_product_async.delay(product_id, **serializer.validated_data)
            cache.delete(f'product_{product_id}')  # Invalidate product cache
            cache.delete('product_list')  # Invalidate product list cache
            return JsonResponse({'message': 'Product update task has been scheduled'}, status=202)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        delete_product_async.delay(product_id)
        cache.delete(f'product_{product_id}')  # Invalidate product cache
        cache.delete('product_list')  # Invalidate product list cache
        return JsonResponse({'message': 'Product deletion task has been scheduled'}, status=202)

# class ProductListCreateAPI(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     @cache_page(60)  # Cache for 60 seconds
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# class ProductRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     @cache_page(60)  # Cache for 60 seconds
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# from .models import Product, Specification
# from config.mongodb_connection import *

# def add_product():
#     product = Product(
#         name="iphone",
#         price=1000,
#         specifications=Specification(size="30*90pixels", color="black"),
#         category_specific_field={'type':"electronics",'os':"ios",'screen protector':'greatone'}
#     )
    
#     product.save()

# add_product()