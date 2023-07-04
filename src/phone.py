from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, quantity_sim: int):
        super().__init__(name, price, quantity)
        self.quantity_sim = quantity_sim

    @property
    def number_of_sim(self):
        return self.quantity_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity_sim):
        if int(quantity_sim) is True and quantity_sim > 0:
            self.quantity_sim = quantity_sim
        else:
            print("Количество физических SIM-карт должно быть целым числом больше нуля")
        return self.quantity_sim

    def __radd__(self, other):
        if isinstance(other, Item):
            return other.quantity + self.quantity
        else:
            print('Складывать можно только объекты Item и дочерние от них.')

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            print('Складывать можно только объекты Item и дочерние от них.')

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.quantity_sim})"

