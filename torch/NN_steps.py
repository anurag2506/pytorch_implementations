'''Putting it all together
Create a simple linear model and perform one optimization step.
Create a random input tensor x and a random target tensor y.
Create weight and bias tensors and manually compute the prediction y_pred.
Compute the Mean Squared Error loss. 
Calculate the gradients using loss.backward() and update the weights manually based on a learning rate.
'''

'''
Normalize a batch of data.
Create a tensor representing a batch of 10 samples, each with 5 features.
Normalize each feature column to have a mean of 0 and a standard deviation of 1, without using nn.BatchNorm1d. 
Use vectorized operations.
'''

'''
Build a custom tensor based on complex logic.
Create a tensor A of shape (100, 100). Use a combination of masking and reduction operations to create a new 1D tensor B. 
For each row in A, if the mean is greater than 0.5, the corresponding element in B should be the sum of that row. 
Otherwise, it should be the maximum value of that row.
'''

'''
Simulate a step in a recurrent network.
Create an input sequence tensor of shape (batch_size, sequence_length, feature_size). 
Create a hidden state tensor of shape (batch_size, feature_size). 
Compute the next hidden state by matrix-multiplying the current input vector (input[:, t, :]) with a weight matrix and adding a bias.
Use a Python loop to simulate one step of a simplified RNN.
'''

'''
Find and replace outliers using clamping and masking.
Create a tensor data of shape (8, 8) with random values.
First, calculate the mean and standard deviation of data.
Define an "outlier" as any value more than two standard deviations away from the mean. 
Create a boolean mask to identify these outliers. 
Then, use a combination of clamping or torch.where to replace the outliers with the mean value.
'''