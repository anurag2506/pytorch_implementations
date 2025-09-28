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


# device = None
# if torch.cuda.is_available():
#     device = "cuda"
# elif torch.backends.mps.is_available():
#     device = "mps"
# else:
#     device = "cpu"
    
    
# b = b.to(device=device)
# assert(b.device == "mps")

c = torch.arange(0,25)
d = torch.reshape(c,shape=(5,5))
d = d.to("mps")
print(d.device)
print(d.shape)
print(d.dtype)
print(d[0,:5])


'''
Difference between torch.linspace and torch.arange
1. Linspace: 
- Defines the number of elements to be generated between start and end intervals
- torch.linspace(start,end,num_elements)

2. Arange:
- Defines the step value between start and end intervals, basically used as a loop
- torch.linspace(start,end,step_size)
'''