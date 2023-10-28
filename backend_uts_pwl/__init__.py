from pyramid.config import Configurator
from pyramid.renderers import JSON

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    
    # Tambahkan routes
    config.add_route('get_products', '/get_products')
    config.add_route('add_product', '/add_product')
    config.add_route('remove_product', '/remove_product/{product_id}')
    
    # Tambahkan konfigurasi CORS
    config.include('pyramid_cors')
    config.add_cors_preflight_handler()
    config.set_cors_policy({
        'allow_origins': ['*'],
        'allow_credentials': True,
        'allow_methods': ['GET', 'POST', 'PUT', 'DELETE'],
        'allow_headers': ['Content-Type'],
    })

    config.scan()
    return config.make_wsgi_app()
