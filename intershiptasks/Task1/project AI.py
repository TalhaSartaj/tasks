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

ssd_case = ["d1","d2"]
ssd_descriptions = ["240 GB SSD", "480 GB SSD"]
ssd_prices = [11,9.99,49.99]

hdd_case = ["e1","e2","e3"]
hdd_description = ["1 TB HDD","2 TB HDD""4 TB HDD"]
hdd_price = [49.99,89.99,129.9]

od_case = ["f1","f2"]
od_description = ["DVD/Blu-Ray Player","DVD/Blu-Ray Re-writer"]
od_prices = [50.00,100.00]

os_case = ["g1","g2"]
os_description = ["Standard Version","Professional Version"]
os_prices = [100.00,175.00]





# Basic set of components cost
basic_components_cost = 200

# Prompt the customer to choose components
print("Welcome to the Online Computer Shop!")
print("Please choose one case, one RAM, and one Main Hard Disk Drive from the following options:")

# Case selection
print("Cases:")
for i in range(len(case_item_codes)):
    print(f"{case_item_codes[i]} - {case_descriptions[i]} (${case_prices[i]})")
selected_case = input("Enter the item code for your chosen case: ")

# RAM selection
print("RAM Options:")
for i in range(len(ram_item_codes)):
    print(f"{ram_item_codes[i]} - {ram_descriptions[i]} (${ram_prices[i]})")
selected_ram = input("Enter the item code for your chosen RAM: ")

# HDD selection
print("Main Hard Disk Drive Options:")
for i in range(len(hdd_item_codes)):
    print(f"{hdd_item_codes[i]} - {hdd_descriptions[i]} (${hdd_prices[i]})")
selected_hdd = input("Enter the item code for your chosen Main Hard Disk Drive: ")

# SSD selection
print("Solid State Drive Options:")
for i in range(len(ssd_case)):
    print(f"{ssd_case[i]} - {ssd_descriptions[i]} (${ssd_prices[i]})")
selected_ssd = input("Enter the item code for your chosen Solid State Drive: ")

# hdd selection
print("Second Hard Disk Drive Options:")
for i in range(len(hdd_item_codes)):
    print(f"{hdd_item_codes[i]} - {hdd_descriptions[i]} (${hdd_prices[i]})")
selected_hdd = input("Enter the item code for your chosen Second Hard Disk Drive: ")

# od selection
print("Optical Drive Options:")
for i in range(len(od_case)):
    print(f"{od_case[i]} - {od_description[i]} (${od_prices[i]})")
selected_od = input("Enter the item code for your chosen Optical Drive: ")

# os selection
print("Operating System Options:")
for i in range(len(os_case)):
    print(f"{os_case[i]} - {os_description[i]} (${os_prices[i]})")
selected_os = input("Enter the item code for your chosen operating system: ")


# Calculate the total price
# Calculate the total price
total_price = basic_components_cost + case_prices[case_item_codes.index(selected_case)] + \
              ram_prices[ram_item_codes.index(selected_ram)] + hdd_prices[hdd_item_codes.index(selected_hdd)] + \
              ssd_prices[ssd_case.index(selected_ssd)] + \
              hdd_prices[hdd_item_codes.index(selected_hdd)] + \
              od_prices[od_case.index(selected_od)] + \
              os_prices[od_case.index(selected_os)]

# Display the chosen items and total price
print("\nYour Chosen Components:")
print(f"Case: {selected_case} - {case_descriptions[case_item_codes.index(selected_case)]}")
print(f"RAM: {selected_ram} - {ram_descriptions[ram_item_codes.index(selected_ram)]}")
print(f"Main Hard Disk Drive: {selected_hdd} - {hdd_descriptions[hdd_item_codes.index(selected_hdd)]}")
print(f"Solid State Drive: {selected_ssd} - {ssd_descriptions[ssd_case.index(selected_ssd)]}")
print(f"Second Hard Disk Drive: {selected_hdd} - {hdd_descriptions[hdd_item_codes.index(selected_hdd)]}")
print(f"Optical Drive: {selected_od} - {od_description[od_case.index(selected_od)]}")
print(f"Operating System: {selected_os} - {os_description[os_case.index(selected_os)]}")

print(f"\nTotal Price: ${total_price}")

