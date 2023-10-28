def includeme(config):
    config.add_route('add_product', '/add_product')
    config.add_route('remove_product', '/remove_product')
    config.scan('.views')
