"""
part2.ipynb

Automatically generated by Colaboratory.

Original file is located at https://colab.research.google.com/drive/1o3-CQaXeTs8iPnA0jK0jdkN9c01iT-u4

# Information
Authors: Shreyans Patel (SSP210009) and Pranitha Sreethar (PXS200095)

Dataset Owner/Donor Information:

Name: Amir Karami

Institutions: University of South Carolina

Email: karami@sc.edu 

Date Donated: 2015 

Dataset Information:

The data was collected in 2015 using Twitter API. This dataset contains health news from more than 15 major health news agencies such as BBC, CNN, and NYT.

References:

1) https://numpy.org/doc/stable/reference/

2) https://pandas.pydata.org/docs/reference/index.html

3) https://docs.python.org/3/library/re.html

4) https://docs.python.org/3/library/random.html

5) https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter
"""

# Library Imports
import pandas as pd
import re as regex
import requests
import random

# Index from which the actual tweet starts. This will enable us to remove tweet id and timestamp without using regex
TWEET_START_INDEX = 50

class K_Means_Clustering:
    def __init__(self, data_file):
        # Get data and split into seperate tweets
        self.raw_input = requests.get(data_file)
        self.raw_input = self.raw_input.text
        self.raw_input = self.raw_input.split('\n')
        
        # Loaded Successfully
        print("Data loaded successfully. Total tweets: ", len(self.raw_input), "\n")

    # Helper Functions Start
    def get_jaccard_dist(self, tweet_1, tweet_2):
        # Take intersection
        intersection = len(list(set(tweet_1).intersection(tweet_2)))

        # Take union
        union = (len(tweet_1) + len(tweet_2)) - intersection
        return float(1 - (intersection / union))

    def clusterize(self, list_of_list_of_tweets, centroids): 
        # Dictionary of clusters
        dict_of_words = {}

        # For tweet_1 and tweet_2, compute their jaccard distance and then add the closest tweets to disctionary
        for tweet_1 in list_of_list_of_tweets:
            jaccard_dist = []
            for tweet_2 in range(len(centroids)):
                jaccard_dist.append(self.get_jaccard_dist(centroids[tweet_2], tweet_1))
            min_dist = jaccard_dist.index(min(jaccard_dist))
            dict_of_words.setdefault(min_dist, [])
            dict_of_words[min_dist].append(tweet_1)
        return dict_of_words 

    def calculate_centroid(self, list_of_list_of_tweets):
        min_dists = {}
        idx = 0
        for tweet_1 in list_of_list_of_tweets:
            list_of_min_dist = []
            for tweet_2 in list_of_list_of_tweets:
                dist = self.get_jaccard_dist(tweet_1, tweet_2)
                list_of_min_dist.append(dist) 
            min_dists[idx] = sum(list_of_min_dist)
            idx = idx + 1
        min_dist_cluster_idx = [(key, value)[0] for key, value in min_dists.items() if value == min(min_dists.values())]
        return list_of_list_of_tweets[min_dist_cluster_idx[0]]

    def calculate_sse_error(self, centroids, clusters):
        sse_error = 0
        # print("Clusters:", clusters.keys())
        # print("Centroids:", centroid)
        for key, value in clusters.items():
            for data_point in value:
                sse_error += self.get_jaccard_dist(centroids[key], data_point)**2

        return sse_error
    # Helper Functions End

    def pre_process(self):
        print("Pre-processing the data\n")
        self.processed_data = []
        
        for tweet in self.raw_input:
            # Remove the tweet id and timestamp
            modified_tweet = tweet[TWEET_START_INDEX:]

            # Remove any word that starts with @
            modified_tweet = regex.sub('@\S+', "", modified_tweet)

            # Remove any hastag symbols from words
            modified_tweet = regex.sub('#', "", modified_tweet)

            # Remove any url 
            modified_tweet = regex.sub('http\S+', '', modified_tweet)

            # Convert every word to lowercase
            modified_tweet = modified_tweet.lower()

            # Also remove any other symbols since we believe it is introducing noise
            modified_tweet = regex.sub(r'[\'’‘\"?,:-]', ' ', modified_tweet)

            # Split the tweet into a list of words
            modified_tweet = modified_tweet.split()

            self.processed_data.append(modified_tweet)
        
        # Check if pre_process is successful by printing first 30 tweets
        for string in self.processed_data[:30]:
            print(string)

        print("\nPre-processed data successfully\n")

    def train(self, k):
        print("\nTraining stage started\n")
        centroids = []
        centroids_new = []
        random_idx = random.sample(range(0, len(self.processed_data) - 1), k)
        # print("Random: ",random_idx) # Check if random is working fine
        for idx in random_idx:
            centroids.append(self.processed_data[idx])
        centroids_old = centroids
        iteration = 1

        while True:
            centroids_new = []
            clusters = self.clusterize(self.processed_data, centroids_old)
            for words in clusters:
                centroids_new.append(self.calculate_centroid(clusters[words]))
            print("SSE Error for iteration", iteration, ":" + str(self.calculate_sse_error(centroids_new,clusters)))
            iteration += 1
            if centroids_old == centroids_new:
                break
            centroids_old = centroids_new
            
        return centroids_new, clusters
        
if __name__ == "__main__":
    # List of hyperparameters and results
    values_of_k_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    size_of_cluster_list = []
    sse_error_list = []

    # Get the data
    KMC = K_Means_Clustering("https://raw.githubusercontent.com/Shreyans1602/Machine_Learning_K_Means_Clustering/main/BBC_Health_Dataset.txt")
    
    # Pre-process the data
    KMC.pre_process()

    # Train
    for k in values_of_k_list:
        centroid, clusters = KMC.train(k)
        size_of_clusters = {}
        for cluster in clusters:
            size_of_clusters[cluster] = len(clusters[cluster])
        size_of_cluster_list.append(size_of_clusters)
        sse_error_list.append(KMC.calculate_sse_error(centroid, clusters))
        print("Final SSE Error: ", KMC.calculate_sse_error(centroid, clusters))

    # Make a table to print results and export a csv
    results_table = pd.DataFrame()
    results_table["Value_of_K"] = values_of_k_list
    results_table["SSE_Error"] = sse_error_list
    results_table["Size_of_Clusters"] = size_of_cluster_list
    results_table.index = results_table.index + 1
    results_table.to_csv('results.csv')
    print("\nPrinting the required output table:\n")
    print(results_table)