# Fuzzy Wire Creations - Order Tracker
# quick script para di ko na kalimutan yung mga orders ko haha

orders = []

def add_order(customer, item, qty, price_each, discount=0):
    subtotal = qty * price_each
    total = subtotal - (subtotal * discount / 100)
    order = {
        "customer": customer,
        "item": item,
        "qty": qty,
        "total": total,
        "discount": discount
    }
    orders.append(order)
    return order

def show_orders():
    print("---- Order List ----")
    for o in orders:
        discount_note = f" ({o['discount']}% off)" if o["discount"] > 0 else ""
        print(f"{o['customer']} - {o['item']} x{o['qty']} = P{o['total']}{discount_note}")

def total_sales():
    return sum(o["total"] for o in orders)

# sample data muna
add_order("Ana", "Rose Bouquet (Small)", 1, 250)
add_order("Miko", "Keychain", 3, 80)
add_order("Jhen", "Bouquet Set (Bulk)", 5, 200, discount=10)

show_orders()
print("Total sales so far: P" + str(total_sales()))