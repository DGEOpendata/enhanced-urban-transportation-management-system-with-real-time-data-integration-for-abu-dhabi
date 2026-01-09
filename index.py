python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load transportation data
transport_data = pd.read_csv('abu_dhabi_transport_data.csv')

# Preprocess data
transport_data.fillna(0, inplace=True)

# Feature selection
features = transport_data[['ridership', 'congestion_level', 'schedule_adherence']]

# Apply KMeans clustering to find congestion patterns
kmeans = KMeans(n_clusters=3)
transport_data['congestion_cluster'] = kmeans.fit_predict(features)

# Visualize the clusters
plt.scatter(transport_data['ridership'], transport_data['congestion_level'], c=transport_data['congestion_cluster'])
plt.xlabel('Ridership')
plt.ylabel('Congestion Level')
plt.title('Congestion Clusters')
plt.show()

# Function to suggest route optimization
def suggest_route_optimization(cluster_data):
    # Analyze cluster data to suggest optimizations
    for cluster in cluster_data['congestion_cluster'].unique():
        cluster_ridership = cluster_data[cluster_data['congestion_cluster'] == cluster]['ridership'].mean()
        cluster_congestion = cluster_data[cluster_data['congestion_cluster'] == cluster]['congestion_level'].mean()
        print(f'Cluster {cluster}: Average Ridership: {cluster_ridership}, Average Congestion: {cluster_congestion}')
        if cluster_congestion > threshold:
            print(f'Suggest optimization for cluster {cluster}')

# Set a threshold for congestion
threshold = 0.7
suggest_route_optimization(transport_data)
