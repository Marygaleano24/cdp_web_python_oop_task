from ownable import Ownable

class Cart:
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            pass  # Eliminar el pass al codificar el método check_out.
        
        # Requisitos:
        #   - El precio de compra de todos los artículos en el carrito (Cart#items) se transfiere 
        #     de la billetera del propietario del carrito a la billetera del propietario del artículo.
        #   - La propiedad de todos los artículos en el carrito (Cart#items) se transfiere al propietario del carrito.
        #   - El contenido del carrito (Cart#items) debe vaciarse.
        
        # Pistas:
        #   - La billetera del propietario del carrito ==> self.owner.wallet
        #   - La billetera del propietario del artículo ==> item.owner.wallet
        #   - Transferencia de dinero ==> retirar de la billetera del propietario del carrito y 
        #     depositar en la billetera del propietario del artículo.
        #   - Transferencia de propiedad del artículo al propietario del carrito ==> cambiar item.owner = self.owner
