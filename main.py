import json


class Store:
    def __init__(self, name, address):
        """Инициализация магазина с названием и адресом."""
        self.name = name
        self.address = address
        self.items = {}  # Словарь товаров

    def add_item(self):
        """Добавляет товар в магазин. Пользователь вводит данные."""
        item_name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self):
        """Удаляет товар из магазина. Пользователь вводит данные."""
        item_name = input("Введите название товара для удаления: ")
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self):
        """Возвращает цену товара по названию. Пользователь вводит данные."""
        item_name = input("Введите название товара для получения цены: ")
        price = self.items.get(item_name)
        if price is None:
            print(f"Товар '{item_name}' не найден.")
        else:
            print(f"Цена на '{item_name}': {price}")

    def update_price(self):
        """Обновляет цену товара. Пользователь вводит данные."""
        item_name = input("Введите название товара для обновления цены: ")
        if item_name in self.items:
            new_price = float(input(f"Введите новую цену для '{item_name}': "))
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def __repr__(self):
        """Отображает информацию о магазине и его товарах."""
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

    def to_dict(self):
        """Конвертирует объект магазина в словарь для сохранения в JSON."""
        return {
            'name': self.name,
            'address': self.address,
            'items': self.items
        }

    @classmethod
    def from_dict(cls, data):
        """Создаёт объект Store из словаря (данные из JSON)."""
        store = cls(data['name'], data['address'])
        store.items = data['items']
        return store


def save_stores_to_file(stores, filename):
    """Сохраняет все магазины в файл JSON."""
    stores_data = {name: store.to_dict() for name, store in stores.items()}
    with open(filename, 'w') as f:
        json.dump(stores_data, f, indent=4)  # Добавлен отступ для лучшего формата
    print(f"Магазины сохранены в файл {filename}.")


def load_stores_from_file(filename):
    """Загружает магазины из файла JSON."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return {name: Store.from_dict(store_data) for name, store_data in data.items()}
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создаются новые магазины.")
        return {}


def main():
    # Загружаем магазины из файла или создаём новые
    filename = "stores_data.json"
    stores = load_stores_from_file(filename)

    while True:
        print("\nМеню:")
        print("1. Создать новый магазин")
        print("2. Переключиться на существующий магазин")
        print("3. Показать все магазины")
        print("4. Сохранить и выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            # Создание нового магазина
            store_name = input("Введите название магазина: ")
            store_address = input("Введите адрес магазина: ")
            stores[store_name] = Store(store_name, store_address)
            print(f"Магазин '{store_name}' создан.")

        elif choice == '2':
            # Переключение на существующий магазин
            store_name = input("Введите название магазина для работы: ")
            if store_name in stores:
                store = stores[store_name]
                while True:
                    print(f"\nВыбран магазин: {store_name}")
                    print("1. Добавить товар")
                    print("2. Получить цену товара")
                    print("3. Обновить цену товара")
                    print("4. Удалить товар")
                    print("5. Показать информацию о магазине")
                    print("6. Вернуться к выбору магазина")
                    sub_choice = input("Выберите действие: ")

                    if sub_choice == '1':
                        store.add_item()
                    elif sub_choice == '2':
                        store.get_price()
                    elif sub_choice == '3':
                        store.update_price()
                    elif sub_choice == '4':
                        store.remove_item()
                    elif sub_choice == '5':
                        print(store)
                    elif sub_choice == '6':
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
            else:
                print(f"Магазин '{store_name}' не найден.")

        elif choice == '3':
            # Показать все магазины
            if stores:
                print("Список магазинов:")
                for store_name in stores:
                    print(f"- {store_name}")
            else:
                print("Магазинов нет.")

        elif choice == '4':
            # Сохранение всех магазинов и выход
            save_stores_to_file(stores, filename)
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
