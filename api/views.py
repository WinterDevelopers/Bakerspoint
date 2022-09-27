from store.models import Product, ProductImage
from api.sterilizer import ProductSerializer, ProductImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

@api_view(['POST'])
def productPageData(request):
    data = json.loads(request.body)
    product_name = data['name']
    product_weight = data['weight']
    product = get_object_or_404(Product, product_category=product_name, weight=product_weight)
    serial_product = ProductSerializer(product, many=False)
    images = ProductImage.objects.filter(product=product.id)
    serial_images = ProductImageSerializer(images, many=True)
    data = {'product_info':serial_product.data,'product_images':serial_images.data}
    return Response(data)


