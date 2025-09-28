'''
Reshaping and viewing a tensor.
Create a random tensor of shape (2, 3, 4). Reshape it to a shape of (4, 6). 
Then, create a view of the original tensor with a shape of (8, 3). 
Explain the key difference between using reshape and view in this context.
'''


'''
Concatenation and stacking tensors.
Create three random tensors, each of shape (2, 4). Concatenate them along the second dimension (dim=1). 
Then, stack them along a new dimension.
Print the shape of the resulting tensors and explain the difference between torch.cat and torch.stack.
'''


'''
Squeezing and unsqueezing dimensions.
Create a random tensor with shape (1, 20, 1, 1, 5). 
Squeeze all the dimensions with size 1. 
Then, unsqueeze a dimension of size 1 at index 1.
Print the shape at each step.
'''

'''
Transposing and permuting a tensor.
Create a random tensor of shape (4, 5, 6). Use permute to swap dimensions 0 and 2.
Then, use .T to transpose the first two dimensions of a 2D slice of the original tensor.
'''