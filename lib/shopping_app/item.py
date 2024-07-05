from ownable import Ownable

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Item, dicha instancia (self) se almacena en la variable de clase instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Devuelve instances ==> Item.item_all() devuelve todas las instancias de Item creadas hasta el momento.
        return Item.instances

