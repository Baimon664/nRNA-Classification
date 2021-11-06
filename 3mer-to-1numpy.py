import numpy as np
names=open("3mer/name.txt",'r')
b=np.array([])

for i in names.readlines():
    i=i.strip()
    a=np.load("3mer/"+i)
    b = np.append(b,a)
    print(i,"finish")
b=b.reshape((95100,198,3))
np.save("3-mer.npy",b)
names.close()