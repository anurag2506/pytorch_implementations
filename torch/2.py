import torch

a = torch.zeros((5,5))
count = 0
for i in range(5):
    for j in range(5):
        a[i,j] = count
        count += 1


# # reshaping the tensor to (25,)
b = torch.reshape(a,shape=(25,))
assert(b.shape == (25,))
b = b*2


device = None
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
    
    
b = b.to(device=device)
assert(b.device == "mps")