def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")
        total_items += quantity
    print(f"Total number of items: {total_items}")

# Sample inventory dictionary
inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

# Display the inventory
display_invent_
