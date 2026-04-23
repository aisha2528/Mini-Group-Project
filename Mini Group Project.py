import pandas as pd
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv('data.csv')

df['Year'] = df['Year'].astype(str).str.strip()

# Summary stats
summary_stats = df.groupby('ResidenceType')[['CarDriver', 'BusOther']].mean()
print("--- Average Trips per Person (2002-2023) ---")
print(summary_stats)

# Bar chart (Urban vs Rural)

data_2023 = df[df['Year'] == "2023"]

print("Rows found for 2023:", len(data_2023))

plt.figure(figsize=(8, 5))
ax = plt.gca()

data_2023.plot(
    kind='bar',
    x='ResidenceType',
    y=['CarDriver', 'BusOther'],
    color=['#1f77b4', '#ff7f0e'],
    ax=ax
)

plt.title('Transport Mode Choice: Car vs Bus (2023)')
plt.ylabel('Average Trips per Person')
plt.xlabel('Area Classification')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('urban_rural_comparison.png')
plt.show()

# Line graph (Trends)

trend_df = df[df['ResidenceType'] == 'All areas']

plt.figure(figsize=(8, 5))
plt.plot(trend_df['Year'], trend_df['CarDriver'], marker='o', label='Car Driver')
plt.plot(trend_df['Year'], trend_df['BusOther'], marker='s', label='Local Bus (Non-London)')

plt.title('UK National Travel Trends: 2002–2023')
plt.ylabel('Trips per Person per Year')
plt.xlabel('Year')
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig('travel_trends_line.png')
plt.show()

# Scatter plot (Walking vs Driving)

plt.figure(figsize=(8, 6))

for label, group in df.groupby('ResidenceType'):
    plt.scatter(group['Walk'], group['CarDriver'], label=label, s=100, alpha=0.7)

plt.title('Correlation: Walking vs Driving Trips')
plt.xlabel('Average Walking Trips per Year')
plt.ylabel('Average Driving Trips per Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('walking_vs_driving_scatter.png')
plt.show()

print("\nSuccess: Three plots (Bar, Line, Scatter) generated and saved.")