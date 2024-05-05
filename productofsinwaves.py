import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,0.01,1)
f1=2
f2=4
x1=np.sin(2*np.pi*f1*t)
x2=np.sin(2*np.pi*f2*t)
x=x1*x2
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

