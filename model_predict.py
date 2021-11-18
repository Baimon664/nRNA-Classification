import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.models.load_model("my_model_v5.h5")

def QMer(seq):
    q=3
    data = []
    for i in range(len(seq)-(q-1)):
        data.append(list(seq[i:i+q]))
    return data

rna = input("RNA:").strip()
p=[]
for i in rna:
    k=0
    if(i=="A"):
        k=1
    elif(i=='U' or i=="T"):
        k=2
    elif(i=='C'):
        k=3
    elif(i=='G'):
        k=4
    p.append(k)
p=p+[0]*(200-len(p))
p=QMer(p)
b=np.array(p)
b=b.reshape((1,198,3))/4
names=open("npy_2/name.txt",'r')
t=model.predict(b)
t1=np.argmax(t)
o = names.readlines()
pred = o[t1][:-5]
print(pred)
names.close()

