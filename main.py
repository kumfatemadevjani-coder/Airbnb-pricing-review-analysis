import pandas as pd

# Load the dataset
df = pd.read_csv("Listings.csv",encoding='latin-1',low_memory=False)
# Display the first few rows of the dataset
#print(df.head(5))
#df.shape
#df.head()
#df.info()


# Check for missing values
#print(df.isnull().sum())
# Fill missing values with the mean of the column
#df['Price'] = df['Price'].fillna(df['Price'].mean())
#name of the columns
#print(df.columns)
#missing_ratio = df.isnull().mean()
#columns_to_drop_missing = missing_ratio[missing_ratio > 0.5].index

#df.drop(columns=columns_to_drop_missing, inplace=True)
df.drop(columns=['host_location'], inplace=True)
df.drop(columns=['listing_id'], inplace=True)
df.drop(columns=['host_id'], inplace=True)

df.drop(columns=['host_response_time'], inplace=True)
df.drop(columns=['district'], inplace=True)
df.drop(columns=['host_response_rate'], inplace=True)
df.drop(columns=['host_acceptance_rate'], inplace=True)



df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].mean())



review_cols = [
    'review_scores_rating',
    'review_scores_accuracy',
    'review_scores_cleanliness',
    'review_scores_checkin',
    'review_scores_communication',
    'review_scores_location',
    'review_scores_value'
]

df[review_cols] = df[review_cols].fillna(0)
df = df.dropna(subset=['name','host_since','host_is_superhost','host_total_listings_count','host_has_profile_pic','host_identity_verified'])


#print(df.isnull().sum())

#df.columns = df.columns.str.lower().str.replace(" ", "_")

df['price'] = (
    df['price']
    .astype(str)
    .str.replace('$','')
    .str.replace(',','')
    .astype(float)
)

df['amenities'] = df['amenities'].str.replace('[{}"]', '', regex=True)

df = df[df['price'] < 500]

df['price_per_person'] = df['price'] / df['accommodates']

df.info()
df.describe()
#save the cleaned dataset to a new CSV file
df.to_csv("airbnb_cleaned.csv", index=False)









