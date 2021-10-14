import numpy as np
x=np.load("all_100.npy")

m=0
for i in x:
    m=max(m,len(i))
print(m)

for i in range(len(x)):
  k=""
  for j in range(len(x[i])):
    if(x[i][j]=="A" or x[i][j]=="a"):
      k+='1'
    elif(x[i][j]=="T" or x[i][j]=="t" or x[i][j]=="U" or x[i][j]=="u"):
      k+='2'
    elif(x[i][j]=="C" or x[i][j]=="c"):
      k+='3'
    elif(x[i][j]=="G" or x[i][j]=="g"):
      k+='4'
  x[i]=k
  print(i)

b=np.array([])
for i in range(len(x)):
    k=[]
    for j in range(len(x[i])):
        k.append(int(x[i][j]))
    p=[0]*(200-len(k))
    k+=p
    k=np.array(k)
    k.reshape((1,200))
    b=np.append(b,k)

b=b.reshape((19020,200)).astype("float32")/4
np.save("x_test_10.npy",b)