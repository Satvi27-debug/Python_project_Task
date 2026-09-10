# =========================================
# SHOPPING CART SYSTEM (FIXED VERSION)
# =========================================

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("\nTuples are immutable")


def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = (total * cart["discount"]) / 100
    return total - discount_amount


# =========================================
# DEMO RUN
# =========================================

print("===== FIXED FUNCTION DEMO =====")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("milk", ["bread"]))
print(add_item_fixed("eggs"))

cart1 = create_cart("Satvendra", 10)
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

cart2 = create_cart("Rahul", 5)
add_to_cart(cart2, "Phone", 25000, 1)
add_to_cart(cart2, "Charger", 1500, 1)

print("\nCustomer 1 Cart:", cart1)
print("Customer 2 Cart:", cart2)

print("\nFinal Total for", cart1["owner"], "=", calculate_total(cart1))
print("Final Total for", cart2["owner"], "=", calculate_total(cart2))

price_data = (500, 600)
update_price(price_data, 1000)
