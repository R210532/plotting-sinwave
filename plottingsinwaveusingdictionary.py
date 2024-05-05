import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
dictionary={"s1":[1,10],"s2":[2,9],"s3":[3,8],"s4":[4,9],"s5":[5,6]}
y=input("enter the sinsidoal key to generate:")
if dictionary[y]:
   x=dictionary[y][0]*np.sin(2*np.pi*dictionary[y][1]*t)
   plt.plot(t,x)
   plt.show()
