import pandas as pd
import time

# Load offers
df = pd.read_csv('data/offers.csv')

print("Starting campaign...\n")

# Loop through customers
for _, row in df.iterrows():
    name = row['name']
    email = row['email']
    offer = row['offer']

    # Simulate sending
    message = f"""
    Hello {name},
    
    We have an exclusive offer for you:
    {offer}
    
    Don't miss out!
    """

    print(f"Sending email to {email}...")
    print(message)
    

with open('data/campaign_log.txt', 'a') as log:
    log.write(f"Sent to {email}: {offer}\n")
    
    # Simulate delay
    time.sleep(1)
    

print("\nCampaign completed successfully!")


