import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv("insurance.csv")

# Select the 6 features you want to use (update these column names)
features = ['age', 'bmi', 'children', 'sex', 'smoker', 'region']  # example
X = df[features]
y = df['charges']  # target variable

# If there are categorical features, encode them
X = pd.get_dummies(X, drop_first=True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open('rf_tuned_6.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as rf_tuned_6.pkl")
