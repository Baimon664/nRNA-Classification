import numpy as np
# names=open("npy_2/name.txt",'r')
# b=np.array([])
# k=0
# for i in names.readlines():
#     i=i.strip()
#     a=np.load("npy_2/"+i)
#     a=a[-20:]
#     b=np.append(b,a)
#     print(i,"finish")
# np.save("all_100.npy",b)
# names.close()

a='GTGCTTTGCTATTTTCATTGACTTCAGGATATCGTGATATTGAGAATTCAATGATGTATAGCAAGGAGCCT'
b=np.array([])
for i in a:
    k=0
    if(i=="A"):
        k=1
    elif(i=='U' or i=="T"):
        k=2
    elif(i=='C'):
        k=3
    elif(i=='G'):
        k=4
    b=np.append(b,k)
k=[0]*(200-len(b))
b=np.append(b,k)
print(b)
b=b.reshape((200,1))
np.save("test.npy",b)
    


import numpy as np
x=np.load("all_100.npy")
m=0
for i in x:
    m=max(m,len(i))
    if(m==399):
        print(i)
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
    else:
      k+='5'
  x[i]=k
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
    print(i)
b=b.reshape((95100,200)).astype("float32")/4
np.save("x_train_10.npy",b)
