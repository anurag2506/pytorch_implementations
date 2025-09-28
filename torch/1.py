import torch

# Creating a random tensor
a = torch.rand(size=(3,4))

# Reshaping it to required dimensions
b = torch.reshape(a,shape=(2,6))

# moving to gpu if available
device = "mps" if torch.backends.mps.is_available() else "cpu"
b = b.to(device=device)
print(b.device)

sum = torch.sum(b)
print(sum)