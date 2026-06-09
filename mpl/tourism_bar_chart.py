import matplotlib.pyplot as plt

# 1. Define the 2025 tourist data directly inside the code (in millions)
countries = ['France', 'Spain', 'Turkey', 'Italy']
tourist_numbers = [105.0, 96.8, 62.0, 61.5]

# Custom professional color palette for each country bar
colors = ['#4a90e2', '#e67e22', '#2ecc71', '#e74c3c']

# 2. Create the bar chart
# 'width' controls the thickness of the bars
plt.bar(countries, tourist_numbers, color=colors, edgecolor='grey', width=0.6)

# 3. Add labels and a title
plt.title('International Tourist Arrivals in 2025\n(2025 Yılı Uluslararası Turist Sayıları)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Countries', fontsize=12, labelpad=10)
plt.ylabel('Number of Tourists in Millions (Milyon Kişi)', fontsize=12, labelpad=10)

# 4. Display exact values dynamically on top of each bar
for i, value in enumerate(tourist_numbers):
    plt.text(i, value + 1.5, f"{value}M", ha='center', va='bottom', fontsize=11, fontweight='bold')

# 5. Fine-tune layout and boundaries
# Set the y-axis limit higher (0 to 120) so text values don't clip at the top
plt.ylim(0, 120)

# Set grid lines for the background (only on the Y axis for clean look)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set the window size (width=10 inches, height=6 inches)
plt.gcf().set_size_inches(10, 6)
plt.tight_layout()

# 6. Open the interactive live pop-up window
print("Opening the bar chart pop-up window...")
plt.show()