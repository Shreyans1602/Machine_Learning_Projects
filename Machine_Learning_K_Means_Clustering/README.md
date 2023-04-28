# Machine_Learning_K_Means_Clustering
In this assignment, you will learn how to cluster tweets by utilizing Jaccard Distance metric and K-means clustering algorithm.

# Tweets Clustering Using K-Means

# Instructions
Twitter provides a service for posting short messages. In practice, many of the tweets are very similar to each other and can be clustered together. By clustering similar tweets together, we can generate a more concise and organized representation of the raw tweets, which will be very useful for many Twitter-based applications (e.g., truth discovery, trend analysis, search ranking, etc.)

# Objectives
- Compute the similarity between tweets using the Jaccard Distance metric.
- Cluster tweets using the K-means clustering algorithm.

# Introduction to Jaccard Distance
The Jaccard distance, which measures dissimilarity between two sample sets (A and B). It is defined as the difference of the sizes of the union and the intersection of two sets divided by the size of the union of the sets.

<img width="495" alt="image" src="https://user-images.githubusercontent.com/66005722/166745524-5bee2f05-4ffa-4f27-9200-22d7726aa7e1.png">

For example, consider the following tweets:

Tweet A: the long march
Tweet B: ides of march

|$A \cap B$| = 1 and |A U B| = 5, therefore the distance is 1 – (1/5)

In this assignment, a tweet can be considered as an unordered set of words such as {a,b,c}. By "unordered", we mean that {a,b,c}={b,a,c}={a,c,b}...

Jaccard Distance Dist(A, B) between tweet A and B has the following properties:
- It is small if tweet A and B are similar.
- It is large if they are not similar.
- It is 0 if they are the same.
- It is 1 if they are completely different (i.e., no overlapping words).

Here is the reference for more details about Jaccard Distance: http://en.wikipedia.org/wiki/Jaccard_index

Hint: Note that since the tweets do not have numerical coordinates as in Euclidean space, you might want to think of a sensible way to compute the "centroid" of a tweet cluster. This could be the tweet having minimum distance to all of the other tweets in a cluster.

# Exercise
Implement the tweet clustering function using the Jaccard Distance metric and K-means clustering algorithm to cluster redundant/repeated tweets into the same cluster. Remember that you have to write your own code for K-means clustering. It is acceptable to use external libraries for data loading and pre-processing only. Python is the preferred language for this assignment. If you want to use any other language, clearly specify how to compile and run your code in the README file.

Note that while the K-means algorithm is proved to converge, the algorithm is sensitive to the k initial selected cluster centroids (i.e., seeds) and the clustering result is not necessarily optimal on a random selection of seeds.

# Steps of the Exercise
1. We are going to use the following dataset for this exercise: https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter. Follow the “Data Folder” link and unzip the given file. You will file a folder containing tweets that contain links to various news sources e.g. the file “usnewshealth.txt” contains tweets that refer to articles published in US News. You have to choose one such file and proceed.

2. Perform the following pre-processing steps:
    - Remove the tweet id and timestamp
    - Remove any word that starts with the symbol @ e.g. @AnnaMedaris
    - Remove any hashtag symbols e.g. convert #depression to depression
    - Remove any URL
    - Convert every word to lowercase 

3. Perform K-means clustering on the resulting tweets using at least 5 different values of K and report your results in the format below. Note that the sum of squared error is defined as:

<img width="250" alt="image" src="https://user-images.githubusercontent.com/66005722/166746515-2af3e772-8b61-4a22-9487-8a0b9859dbe5.png">

where K is the number of clusters and mi is the centroid of the ith cluster.

Value of
K
SSE Size of each cluster
10 200 1: 10 tweets
2: 25 tweets
3: 20 tweets
….
10: 100 tweets
….

| Value of K | SSE | Size of Each Cluster |
| --------------- | --------------- | --------------- |
| 10 | 200 | 1: 10 tweets 2: 25 tweets 3: 20 tweets 10: 100 tweets |       
|  |  |  |
| ... | ... | ... |

# What to Submit
- Table of results as mentioned earlier.
- The source code including a README file indicating how to run your code.
