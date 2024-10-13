# Restaurant Menu Program
def display_menu():
    menu = {
        "Pizza": 8.99,
        "Burger": 5.49,
        "Pasta": 7.99,
        "Salad": 4.99,
        "Fries": 2.99
    }
    
    print("Restaurant Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def take_order():
    menu = {
        "Pizza": 8.99,
        "Burger": 5.49,
        "Pasta": 7.99,
        "Salad": 4.99,
        "Fries": 2.99
    }
    
    order = []
    total = 0.0
    
    while True:
        item = input("Enter the item to order (or 'done' to finish): ").title()
        if item == 'Done':
            break
        elif item in menu:
            order.append(item)
            total += menu[item]
            print(f"{item} added to your order.")
        else:
            print("Sorry, we don't have that item.")
    
    print("\nYour order summary:")
    for item in order:
        print(item)
    print(f"Total: ${total:.2f}")

# Run the program
display_menu()
take_order()
