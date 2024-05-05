import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,0.01,1)
f1=2
f2=3
x=np.sin(2*np.pi*f1*t)
y=np.sin(2*np.pi*f2*t)
z=x+y
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("sinwave")
plt.plot(t,z)
plt.show()

