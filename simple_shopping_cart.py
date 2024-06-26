# simple_shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})

    def total_price(self):
        return sum(item['price'] for item in self.items)

    def view_cart(self):
        return self.items

if __name__ == "__main__":
    cart = ShoppingCart()
    while True:
        action = input("Choose action: add, view, total, or quit: ").strip().lower()
        if action == 'add':
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            cart.add_item(item, price)
        elif action == 'view':
            items = cart.view_cart()
            print("Shopping Cart:")
            for item in items:
                print(f"{item['item']}: ${item['price']:.2f}")
        elif action == 'total':
            print(f"Total price: ${cart.total_price():.2f}")
        elif action == 'quit':
            break
