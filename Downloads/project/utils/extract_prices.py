def extract_prices(products):
    prices = []
    for i in range(len(products)):
        prices.append(products[i].price)
    return prices
