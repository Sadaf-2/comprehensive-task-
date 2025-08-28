
print("Welcome to Crop Yield Analyzer")
farmer_name = "Sadaf"
farm_size_acres = 12.5  
main_crop = "Wheat"
num_fields = 3         
average_yield = 2.8      
is_organic = True        
farm_location = "Valley" 
print("\nFarmer Details:")
print("Name:", farmer_name)
print("Farm Size (acres):", farm_size_acres)
print("Main Crop:", main_crop)
print("Number of Fields (int):", num_fields)
print("Average Yield (tons/acre) (float):", average_yield)
print("Is Organic (bool):", is_organic)
print("Farm Location (string):", farm_location)
if farm_size_acres > 10:
    print("Farm Type: Large farm")
else:
    print("Farm Type: Small farm")
sample_crops = []
for crop in ["Wheat", "Rice", "Corn"]:
    sample_crops.append(crop)

print("\nSample Crop List:")
for crop in sample_crops:
    print("-", crop)
