import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('lazada.csv')

# Define a function to extract the numeric values from the "sold" column
def extract_sold_count(sold_str):
    if isinstance(sold_str, str):
        try:
            # Extract the numeric part of the string, remove commas, dots, and any non-numeric characters
            numeric_str = ''.join(filter(str.isdigit, sold_str))
            # Convert the numeric string to an integer
            sold_count = int(numeric_str)
            return sold_count
        except ValueError:
            # Handle cases where conversion fails (e.g., if the format is not as expected)
            return None
    else:
        # Return the original value if it's already a numeric value (float or int)
        return sold_str
# Apply the extract_sold_count function to the "sold" column
df['Sold'] = df['Sold'].apply(extract_sold_count).astype('Int64')

# Define a function to extract the numeric values from a string
def extract_numeric_value(price_str):
    try:
        # Split the string at the ' ₫' symbol and remove any commas
        numeric_str = price_str.split('₫')[0].replace(',', '')
        # Convert the numeric string to an integer or float
        numeric_value = float(numeric_str)*1000
        return numeric_value
    except ValueError:
        # Handle cases where conversion fails (e.g., if the format is not as expected)
        return None

# Apply the extract_numeric_value function to the 'prices' column
df['Price'] = df['Price'].apply(extract_numeric_value)

def extract_review_count(review_str):
    if isinstance(review_str, str):
        try:
            # Extract the numeric part of the string, remove parentheses and any non-numeric characters
            numeric_str = ''.join(filter(str.isdigit, review_str))
            # Convert the numeric string to an integer
            review_count = int(numeric_str)
            return review_count
        except ValueError:
            # Handle cases where conversion fails (e.g., if the format is not as expected)
            return None
    else:
        # Return the original value if it's already a numeric value (float or int)
        return review_str

# Apply the extract_review_count function to the "review" column
df['Review'] = df['Review'].apply(extract_review_count).astype('Int64')

# Save the DataFrame with the extracted values to a new CSV file
df.to_csv('lazada_extracted.csv', index=False)

# Now, you have a new CSV file named 'shopee_with_numeric_prices.csv'
