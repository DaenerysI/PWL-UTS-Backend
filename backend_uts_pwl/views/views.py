from pyramid.view import view_config
from pyramid.response import Response
import json

@view_config(route_name='get_products', renderer='json')
def get_products(request):
    with open('myproject/products.json') as f:
        products = json.load(f)
    return products

@view_config(route_name='add_product', renderer='json', request_method='POST')
def add_product(request):
    # Logika untuk menambah produk ke database
    data = json.loads(request.body)
    # Proses tambah produk ke database
    return Response(json.dumps({"message": "Product added successfully"}))

@view_config(route_name='remove_product', renderer='json', request_method='POST')
def remove_product(request):
    # Logika untuk menghapus produk dari database
    data = json.loads(request.body)
    # Proses hapus produk dari database
    return Response(json.dumps({"message": "Product removed successfully"}))