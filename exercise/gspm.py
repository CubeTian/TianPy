import numpy as np
from numpy import sin,cos,linspace
import matplotlib.pyplot as plt
# a = array([1,2,3])
# b = array([3,2,1])
# c = cross(a, b)
# print(c)
x = linspace(0,1,21,dtype=np.float)

f1 = cos(x**2*(1-x)**2)*cos(t)
print(x)

plt.figure(1)
plt.plot(x,me,label='me')
plt.legend(loc='upper right')
plt.show()
