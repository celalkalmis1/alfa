import matplotlib.pyplot as plt

# 1. Define the data directly inside the code (No external CSV needed)
# Labels for the sectors
labels = ['Agriculture', 'Industry', 'Services']

# GDP sector shares for Turkey and Spain (in percentages)
turkey_shares = [6.5, 27.5, 66.0]
spain_shares = [2.7, 22.0, 75.3]

# Soft and professional color palette for the pie slices
colors = ['#ff9999', '#66b3ff', '#99ff99']

# 2. Plot the first pie chart (Turkey)
# subplot(rows, columns, panel_number) -> 1 row, 2 columns, 1st panel
plt.subplot(1, 2, 1)
plt.pie(turkey_shares, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Turkey GDP by Sector', fontsize=14, fontweight='bold')

# 3. Plot the second pie chart (Spain)
# subplot(rows, columns, panel_number) -> 1 row, 2 columns, 2nd panel
plt.subplot(1, 2, 2)
plt.pie(spain_shares, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Spain GDP by Sector', fontsize=14, fontweight='bold')

# 4. Adjust figure layout and dimensions for the pop-up window
# Set the pop-up window size (width=12 inches, height=6 inches)
plt.gcf().set_size_inches(12, 6)

# Automatically adjust padding to prevent labels from overlapping
plt.tight_layout()

# 5. Display the chart as a live pop-up window
# This command stops code execution and opens the interactive chart on your screen
print("Opening the pop-up window...")
plt.show()