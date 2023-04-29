class Good:
    def __init__(self, url, price, median_price):
        self.url = url
        self.price = price
        self.median_price = median_price
    def __int__(self, url):
        self.url = url
        self.price = 0
        self.median_price = 0