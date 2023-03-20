def select_products_by_category(products, category):
    result = []
    for product in products:
        if product.category == category:
            result.append(product) #кажется, это супер неэффективно. Хочется хранить это в бд или в map

    return result

