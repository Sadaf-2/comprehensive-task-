# 1. Store the dataset as a list of dictionaries
crop_data = [
    {"Farmer": "Ali", "Crop": "Wheat", "Acres": 5, "Yield": 12, "Region": "North"},
    {"Farmer": "Sana", "Crop": "Rice", "Acres": 8, "Yield": 18, "Region": "South"},
    {"Farmer": "Imran", "Crop": "Corn", "Acres": 4, "Yield": 9, "Region": "East"},
    {"Farmer": "Ayesha", "Crop": "Wheat", "Acres": 6, "Yield": 14, "Region": "West"}
]

# 2a. Print all farmers growing Wheat
print("Farmers growing Wheat:")
for record in crop_data:
    if record["Crop"].lower() == "wheat":
        print("-", record["Farmer"])

# 2b. Calculate total yield across all farmers
total_yield = 0
for record in crop_data:
    total_yield += record["Yield"]

print("\nTotal yield from all farmers:", total_yield, "tons")

# 2c. Find the farmer with the maximum yield
max_yield = 0
top_farmer = ""

for record in crop_data:
    if record["Yield"] > max_yield:
        max_yield = record["Yield"]
        top_farmer = record["Farmer"]

print("\nFarmer with maximum yield:")
print(f"{top_farmer} with {max_yield} tons")
