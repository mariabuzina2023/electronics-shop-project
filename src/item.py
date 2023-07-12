import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    file_csv = '../src/items.csv'
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(cls.file_csv, newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = []
                for i in reader:
                    try:
                        if len(i) != 3 or i.get('name') is None or i.get('price') is None or i.get('quantity') is None:
                            raise InstantiateCSVError
                    except InstantiateCSVError as err:
                        print(err.message)
                        break
                    else:
                        cls(i['name'], i['price'], i['quantity'])

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(value):
        float_value = float(value)
        return int(float_value)

