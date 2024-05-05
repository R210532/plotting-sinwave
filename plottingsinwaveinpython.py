import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,0.01,1)
f=5
x=np.sin(2*np.pi*f*t)
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

