# Machine_Learning_Neural_Networks

# Instructions
In this part, you will write code to optimize the performance of a neural net by trying various combination of hyper-parameters and evaluating their results.

A template code has been provided for your reference. You do not need to follow it exactly, if you can come up with a better solution. The class NeuralNet
contains the code necessary for this assignment.

Below are the requirements and suggested steps of the program:

- In the main method, the program passes path to the data file. Be sure to point that to a network path that your program can access.

- In the preprocess method, you are required to do standard pre-processing tasks such as handling null values, ensuring data integrity, and standardization of attributes.

- Complete the train evaluate method. Perform at least the following steps:
  - Create different neural networks with all possible combination of hyperparameters specified. You are free to use any library or package
  that creates the neural network for you using the chosen combination of hyperparameters.
  - Keep track of model history i.e. model performance (accuracy) vs number of epochs in every case. Plot the model history for all the cases on a single plot. If that becomes too congested, you can break it up into two or three parts, and plot each part on the same plot.
  - Output a table of results containing following columns: model hyperparameters, training and test accuracies, and training and test errors
  (e.g. mean squared error).

# Dataset
You can use any one dataset from the UCI ML repository: https://archive.ics.uci.edu/ml/datasets.php. Note: If the above direct link does not work, you can just Google the UCI ML repository

# What to Submit
- Link to the dataset used. Please do not include the data as part of you submission.
- Your source code and a README file indicating how to run your code. Do not hardcode any paths to your local computer. It is fine to code any public paths, such as AWS S3.
- Model history plots for every model. Model history is a plot of accuracy against the number of epochs.
- Output for your dataset summarized in a tabular format for different combination of parameters.
- A brief report summarizing your results. For example, which activation function performed the best and why do you think so.
- Any assumptions that you made.
