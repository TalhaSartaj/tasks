# ... (Previous code for Task 1)

# Additional items
additional_items_price = 0
additional_items = []

# Ask if the customer wants to purchase additional items
additional_items_choice = input("Do you want to purchase additional items from other categories? (yes/no): ")

if additional_items_choice.lower() == "yes":
    # Define arrays to store component information
    case_item_codes = ["A1", "A2"]
    case_descriptions = ["Compact Tower", "Full Tower"]
    case_prices = [75, 105]

    ram_item_codes = ["B1", "B2", "B3"]
    ram_descriptions = ["8GB", "16GB", "32GB"]
    ram_prices = [79, 149, 299]

    hdd_item_codes = ["C1", "C2", "C3"]
    hdd_descriptions = ["1TB HDD", "2TB HDD", "4TB HDD"]
    hdd_prices = [49, 89, 129]

    ssd_case = ["d1", "d2"]
    ssd_descriptions = ["240 GB SSD", "480 GB SSD"]
    ssd_prices = [11, 9.99, 49.99]

    hdd_case = ["e1", "e2", "e3"]
    hdd_description = ["1 TB HDD", "2 TB HDD""4 TB HDD"]
    hdd_price = [49.99, 89.99, 129.9]

    od_case = ["f1", "f2"]
    od_description = ["DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer"]
    od_prices = [50.00, 100.00]

    os_case = ["g1", "g2"]
    os_description = ["Standard Version", "Professional Version"]
    os_prices = [100.00, 175.00]

    while True:
        print("Additional Item Categories:")
        # Display additional item categories and their options

        # Prompt the customer to choose additional items
        category_choice = input("Enter the category code (or 'done' to finish): ")
        if category_choice.lower() == "done":
            break
        else:
            # Get the item code for the selected additional item
            item_code = input(f"Enter the item code for your chosen {category_choice} item: ")
            additional_items.append(f"{category_choice} - {item_code}")
            additional_items_price += price_of_selected_item

# Calculate the total price with additional items
total_price += additional_items_price

# Display the chosen items and total price
print("\nYour Chosen Components:")
# Display chosen components as before

if additional_items:
    print("\nAdditional Items:")
    for item in additional_items:
        print(item)

print(f"\nTotal Price: ${total_price}")
