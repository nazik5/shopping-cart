class Product:
    def __init__(self, name="", price=0.0, description="", image="", discountPercent=0, id=0, type="", stock=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
        self.id = id
        self.type = type
        self.description = description
        self.image = image
        self.stock = stock

    def getDiscountAmount(self):
        discountAmount = self.price * self.discountPercent / 100
        return round(discountAmount, 2)

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        return round(discountPrice, 2)

    def print(self):
        print(self.name + " - " + str(self.price))