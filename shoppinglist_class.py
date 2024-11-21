from shopping_item import ShoppingItem

item = ShoppingItem("Laptop", 1200, 2)

print(f"The total cost for {item.quantity} {item.name}s is {item.total_cost()}")
