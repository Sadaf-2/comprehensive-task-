# Sample dataset (with one missing yield to demonstrate error handling)
crop_data = [
    {"Farmer": "Ali", "Crop": "Wheat", "Acres": 5, "Yield": 12, "Region": "North"},
    {"Farmer": "Sana", "Crop": "Rice", "Acres": 8, "Yield": 18, "Region": "South"},
    {"Farmer": "Imran", "Crop": "Corn", "Acres": 4, "Yield": 9, "Region": "East"},
    {"Farmer": "Ayesha", "Crop": "Wheat", "Acres": 6, "Yield": 14, "Region": "West"},
    {"Farmer": "Zara", "Crop": "Rice", "Acres": 7, "Region": "South"}  # Missing 'Yield'
]

# Function to calculate average yield per crop type
def average_yield_per_crop(data):
    crop_totals = {}
    crop_counts = {}

    for record in data:
        try:
            crop = record["Crop"]
            yield_value = record["Yield"]
            crop_totals[crop] = crop_totals.get(crop, 0) + yield_value
            crop_counts[crop] = crop_counts.get(crop, 0) + 1
        except KeyError:
            print(f"Warning: Missing yield for farmer '{record.get('Farmer', 'Unknown')}'. Skipping.")

    print("\nAverage Yield per Crop:")
    for crop in crop_totals:
        avg = crop_totals[crop] / crop_counts[crop]
        print(f"- {crop}: {avg:.2f} tons")

# Function to count how many farmers are in each region
def count_farmers_per_region(data):
    region_counts = {}
    for record in data:
        region = record.get("Region", "Unknown")
        region_counts[region] = region_counts.get(region, 0) + 1

    print("\nNumber of Farmers per Region:")
    for region, count in region_counts.items():
        print(f"- {region}: {count} farmer(s)")

# Run the functions
average_yield_per_crop(crop_data)
count_farmers_per_region(crop_data)
