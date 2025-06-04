import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv('company_sales_data.csv')

# Task 1: Line chart for total profit
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'])
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Monthly Total Profit')
plt.grid(True)
plt.savefig('task1_total_profit.png')
plt.close()

# Task 2: Line chart with styling for total units
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_units'],
         linestyle='--', color='red', linewidth=3,
         marker='o', markerfacecolor='red')
plt.xlabel('Month Number')
plt.ylabel('Total Units')
plt.title('Monthly Total Units Sold')
plt.grid(True)
plt.legend(['Total Units'], loc='lower right')
plt.savefig('task2_total_units_styled.png')
plt.close()

# Task 3.1: Line chart for all products on one plot
plt.figure(figsize=(12, 7))
plt.plot(data['month_number'], data['facecream'], label='Face Cream', marker='o')
plt.plot(data['month_number'], data['facewash'], label='Face Wash', marker='v')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste', marker='^')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap', marker='s')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo', marker='d')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer', marker='*')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Monthly Sales of All Products')
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig('task3_all_products_one_plot.png')
plt.close()

# Task 3.2: Separate subplot for each product
fig, axs = plt.subplots(3, 2, figsize=(15, 12))
fig.suptitle('Monthly Sales Data for Each Product', fontsize=16)

axs[0, 0].plot(data['month_number'], data['facecream'], color='blue', marker='o')
axs[0, 0].set_title('Face Cream')
axs[0, 0].set_xlabel('Month Number')
axs[0, 0].set_ylabel('Units Sold')
axs[0, 0].grid(True)

axs[0, 1].plot(data['month_number'], data['facewash'], color='orange', marker='v')
axs[0, 1].set_title('Face Wash')
axs[0, 1].set_xlabel('Month Number')
axs[0, 1].set_ylabel('Units Sold')
axs[0, 1].grid(True)

axs[1, 0].plot(data['month_number'], data['toothpaste'], color='green', marker='^')
axs[1, 0].set_title('Toothpaste')
axs[1, 0].set_xlabel('Month Number')
axs[1, 0].set_ylabel('Units Sold')
axs[1, 0].grid(True)

axs[1, 1].plot(data['month_number'], data['bathingsoap'], color='red', marker='s')
axs[1, 1].set_title('Bathing Soap')
axs[1, 1].set_xlabel('Month Number')
axs[1, 1].set_ylabel('Units Sold')
axs[1, 1].grid(True)

axs[2, 0].plot(data['month_number'], data['shampoo'], color='purple', marker='d')
axs[2, 0].set_title('Shampoo')
axs[2, 0].set_xlabel('Month Number')
axs[2, 0].set_ylabel('Units Sold')
axs[2, 0].grid(True)

axs[2, 1].plot(data['month_number'], data['moisturizer'], color='brown', marker='*')
axs[2, 1].set_title('Moisturizer')
axs[2, 1].set_xlabel('Month Number')
axs[2, 1].set_ylabel('Units Sold')
axs[2, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('task3_separate_subplots.png')
plt.close()

# Task 4: Scatter plot for toothpaste sales
plt.figure(figsize=(10, 6))
plt.scatter(data['month_number'], data['toothpaste'])
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Toothpaste Sales Data')
plt.grid(True, linestyle='--')
plt.savefig('task4_toothpaste_scatter.png')
plt.close()

# Task 5: Bar chart for facecream and facewash
plt.figure(figsize=(12, 7))
x = data['month_number']
width = 0.35
plt.bar(x - width/2, data['facecream'], width, label='Face Cream')
plt.bar(x + width/2, data['facewash'], width, label='Face Wash')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales Data')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('task5_bar_chart.png')
plt.close()

# Task 6: Pie chart for yearly sales of each product
plt.figure(figsize=(10, 8))
product_columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
product_names = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
yearly_sales = [data[product].sum() for product in product_columns]

plt.pie(yearly_sales, labels=product_names, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Yearly Sales Distribution by Product')
plt.savefig('task6_pie_chart.png')
plt.close()

# Task 7: Stacked plot for all products
plt.figure(figsize=(12, 8))
months = data['month_number']
plt.stackplot(months,
              data['facecream'],
              data['facewash'],
              data['toothpaste'],
              data['bathingsoap'],
              data['shampoo'],
              data['moisturizer'],
              labels=product_names)
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Stacked Plot of All Products')
plt.legend(loc='upper left')
plt.grid(True)
plt.savefig('task7_stacked_plot.png')
plt.close()

# Task 8: Layout of subplots
fig = plt.figure(figsize=(15, 10))

# Define grid specification
gs = fig.add_gridspec(3, 3)

# Create subplots
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1:])
ax3 = fig.add_subplot(gs[1, :2])
ax4 = fig.add_subplot(gs[1:, 2])
ax5 = fig.add_subplot(gs[2, 0])
ax6 = fig.add_subplot(gs[2, 1])

# Add titles to each subplot to identify them
ax1.set_title('Subplot 1')
ax2.set_title('Subplot 2')
ax3.set_title('Subplot 3')
ax4.set_title('Subplot 4')
ax5.set_title('Subplot 5')
ax6.set_title('Subplot 6')

# Set the layout
plt.tight_layout()
plt.savefig('task8_subplot_layout.png')
plt.close()

print("All visualizations have been saved successfully.")