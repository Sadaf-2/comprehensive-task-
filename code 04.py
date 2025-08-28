# Script: Crop Yield Analyzer

# 1. Print a welcome message
print("Welcome to Crop Yield Analyzer")

# 2. Variables to store farmer details
farmer_name = "Sadaf"
farm_size_acres = 12.5  # float
main_crop = "Wheat"

# 3. Demonstrating data types
num_fields = 3           # Integer
average_yield = 2.8      # Float
is_organic = True        # Boolean
farm_location = "Valley" # String

# Print farmer details and data types
print("\nFarmer Details:")
print("Name:", farmer_name)
print("Farm Size (acres):", farm_size_acres)
print("Main Crop:", main_crop)
print("Number of Fields (int):", num_fields)
print("Average Yield (tons/acre) (float):", average_yield)
print("Is Organic (bool):", is_organic)
print("Farm Location (string):", farm_location)

# 4. Conditional check on farm size
if farm_size_acres > 10:
    print("Farm Type: Large farm")
else:
    print("Farm Type: Small farm")

# 5. Loop to generate a sample list of crops
sample_crops = []
for crop in ["Wheat", "Rice", "Corn"]:
    sample_crops.append(crop)

print("\nSample Crop List:")
for crop in sample_crops:
    print("-", crop)
