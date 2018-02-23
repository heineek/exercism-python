class Allergies(object):
    def __init__(self, score):
        self._products = []
        if score > 255:
            score = score % 256
        if score & 128 == 128:
            self._products.append("cats")
        if score & 64 == 64:
            self._products.append("pollen")
        if score & 32 == 32:
            self._products.append("chocolate")
        if score & 16 == 16:
            self._products.append("tomatoes")
        if score & 8 == 8:
            self._products.append("strawberries")
        if score & 4 == 4:
            self._products.append("shellfish")
        if score & 2 == 2:
            self._products.append("peanuts")
        if score & 1 == 1:
            self._products.append("eggs")

    def __str__(self):
        return str(self._products)

    def is_allergic_to(self, product):
        return product in self._products

    @property
    def lst(self):
        return self._products