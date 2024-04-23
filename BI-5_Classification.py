import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("/content/seattle-weather.csv")
df = pd.DataFrame(data)

# Convert 'weather' column to binary classification
df['is_rain'] = (df['weather'] == 'rain').astype(int)

# Drop 'weather' column
df = df.drop(columns=['weather'])

# Encode date
df['date'] = pd.to_datetime(df['date']).dt.dayofyear

# Split data into features and target variable
X = df.drop(columns=['is_rain'])
y = df['is_rain']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
