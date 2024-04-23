import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features for K-means clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to the dataframe
df['cluster'] = kmeans.labels_

# Plot clusters
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap='viridis')
plt.xlabel('Standardized Date')
plt.ylabel('Standardized Features')
plt.title('K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()
