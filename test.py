import numpy as np

a=np.arange(1,31).reshape((3,5,2))
b=np.moveaxis(a,-1,0)
print(b.shape[:-1])