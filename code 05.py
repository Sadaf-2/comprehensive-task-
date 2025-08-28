# --- IMPORTS ---
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# --- SAMPLE DATA ---
crop_data = [
    {"Farmer": "Ali", "Crop": "Wheat", "Acres": 5, "Yield": 12, "Region": "North"},
    {"Farmer": "Sana", "Crop": "Rice", "Acres": 8, "Yield": 18, "Region": "South"},
    {"Farmer": "Imran", "Crop": "Corn", "Acres": 4, "Yield": 9, "Region": "East"},
    {"Farmer": "Ayesha", "Crop": "Wheat", "Acres": 6, "Yield": 14, "Region": "West"},
    {"Farmer": "Zara", "Crop": "Rice", "Acres": 7, "Yield": 16, "Region": "South"},
]

# --- CONVERT TO PANDAS DATAFRAME ---
df = pd.DataFrame(crop_data)

# --- TABLE VIEW ---
print("\n=== CROP YIELD DATA ===")
print(df.to_string(index=False))

# --- 1. BAR CHART: Average Yield per Crop ---
avg_yield_per_crop = df.groupby('Crop')['Yield'].mean()
plt.figure(figsize=(6,4))
avg_yield_per_crop.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Yield per Crop')
plt.ylabel('Yield (tons)')
plt.xlabel('Crop')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- 2. PIE CHART: Percentage of Farmers by Region ---
region_counts = df['Region'].value_counts()
plt.figure(figsize=(6,6))
region_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Percentage of Farmers by Region')
plt.ylabel('')
plt.tight_layout()
plt.show()

# --- 3. SCATTER PLOT: Acres vs Yield ---
plt.figure(figsize=(6,4))
plt.scatter(df['Acres'], df['Yield'], color='green')
plt.title('Acres vs Yield')
plt.xlabel('Acres')
plt.ylabel('Yield (tons)')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 4. CORRELATION ANALYSIS ---
correlation, _ = pearsonr(df['Acres'], df['Yield'])
print(f"\nCorrelation (Acres vs Yield): {correlation:.2f}")

# --- 5. SIMPLE YIELD PREDICTION MODEL ---
# Predicted Yield = Acres × Average Yield per Acre (dataset-wide)
average_yield_per_acre = (df['Yield'].sum()) / (df['Acres'].sum())
df['Predicted_Yield'] = df['Acres'] * average_yield_per_acre

# --- DISPLAY FINAL TABLE WITH PREDICTION ---
print("\n=== PREDICTED YIELDS ===")
print(df[['Farmer', 'Acres', 'Yield', 'Predicted_Yield']].round(2).to_string(index=False))
