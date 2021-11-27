import numpy as np
names=open("npy_2/name.txt",'r')
m=[]

q=3
def QMer(seq):
    data = []
    for i in range(len(seq)-(q-1)):
        data.append(list(seq[i:i+q]))
    return data

for i in names.readlines():
  i=i.strip()
  a=np.load("npy_2/"+i)
  for z in range(100):
    k=""
    p = a[z]
    for j in range(len(p)):
      if(p[j]=="A" or p[j]=="a"):
        k+='1'
      elif(p[j]=="T" or p[j]=="t" or p[j]=="U" or p[j]=="u"):
        k+='2'
      elif(p[j]=="C" or p[j]=="c"):
        k+='3'
      elif(p[j]=="G" or p[j]=="g"):
        k+='4'
      else:
        k+='0'
    k+="0"*(200-len(k))
    data = QMer(k)
    m.append(data)
  print(i,"finish")
b=np.array(m)
np.save("3mer.npy",b)
