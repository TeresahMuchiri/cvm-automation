import pandas as pd
import random

# Load offers
df = pd.read_csv('data/offers.csv')

# Simulate campaign results
df['opened'] = [random.choice([0, 1]) for _ in range(len(df))]
df['clicked'] = [random.choice([0, 1]) for _ in range(len(df))]
df['converted'] = [random.choice([0, 1]) for _ in range(len(df))]

# Save results
df.to_csv('data/campaign_results.csv', index=False)

print("Campaign results generated!")
print(df)

total = len(df)
open_rate = df['opened'].sum() / total
click_rate = df['clicked'].sum() / total
conversion_rate = df['converted'].sum() / total

print(f"Open Rate: {open_rate:.2f}")
print(f"Click Rate: {click_rate:.2f}")
print(f"Conversion Rate: {conversion_rate:.2f}")