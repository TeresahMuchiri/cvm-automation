import pandas as pd

# Load customer data
df = pd.read_csv('data/customers.csv')

# Function to generate offers
def generate_offer(row):
    if row['spend'] > 500:
        return "Premium Discount 20%"
    elif row['last_active_days'] > 20:
        return "We Miss You - 30% Off"
    else:
        return "Standard Offer 10%"

# Apply logic
df['offer'] = df.apply(generate_offer, axis=1)

# Save output
df.to_csv('data/offers.csv', index=False)

print("Offers generated successfully!")
print(df)
