import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result
    
result_tmp = []
num = 0.2
q1 = np.array([0.5,0.55,0.6,0.65,0.7])
k1 = np.array([0.95,0.96,0.97,0.98])
k2 = np.array([0.97,0.98,0.99])
a = num
b = 0.65
for i in q1:
    for j in k1:
        for k in k2:
            result_tmp.append(a*j*i+b*k*(1-i))

result = all_list(result_tmp)
count = 0
x = np.arange(len(result),dtype=np.float)
y = np.arange(len(result),dtype=np.float)
for key in sorted(result):
    x[count] = key
    y[count] = result[key]
    count = count + 1

plt.figure(1)

plt.hist(result_tmp, bins=50)
sns.kdeplot(result_tmp,bw=0.02,shade=True)
plt.plot(x,y,marker='.',label=str(num))
plt.legend(loc='upper right')
plt.grid('on')
plt.show()
# for s in np.array(result):
#     print('%.2f\n' % s)
