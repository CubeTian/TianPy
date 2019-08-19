import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

def plot1(x,f):
    plt.figure()
    plt.plot(x,f)
    plt.show()
from mpl_toolkits.mplot3d import axes3d
n = 20
xall=np.linspace(0,1,n+2)
x=xall[1:n+1]
f=np.arange(n,dtype=float)
ure=np.arange(n+2,dtype=float)
D=np.arange(n,dtype=float)
D_1=np.arange(n-1,dtype=float)
for i in range(n+2):
     ure[i] =np.sinh(np.sin(np.pi*xall[i]))
for i in range(n):
    f[i]=np.pi**2*np.sin(np.pi*x[i])*np.cosh(np.sin(np.pi*x[i]))
    D[i]=2/x[0]**2+np.pi**2*np.cos(np.pi*x[i])**2

for i in range(n-1):
    D_1[i]=-1/x[0]**2

A = np.diag(D)+np.diag(D_1,k=1)+np.diag(D_1,k=-1)
g = inv(A).dot(f.T).T

plt.figure(1)
plt.plot(x,g,label='g')
plt.plot(xall,ure,label='ure')
plt.legend(loc='upper right')
plt.show()







def FIGPLT3(x,y,z):
    x, y = np.meshgrid(x,y)
    #z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
    ax = plt.gca(projection='3d')  # 返回的对象就是导入的axes3d类型对象
    plt.title('3D Surface', fontsize=20)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_zlabel('z', fontsize=14)
    plt.tick_params(labelsize=10)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='spring')
    plt.show()

