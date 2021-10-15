import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.models.load_model("my_model_v2.h5")

rna = input("RNA:").strip()
# fam = input("RFAM class (only num): ").strip()
# fam = "RF"+"0"*(5-len(fam))+fam
b=np.array([])
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
    b=np.append(b,k)
k=[0]*(200-len(b))
b=np.append(b,k)
b=b.reshape((1,200,1))/4
names=open("npy_2/name.txt",'r')
t=model.predict(b)
t1=np.argmax(t)
o = names.readlines()
pred = o[t1][:-5]
# print(pred,pred==fam)
print(pred)
names.close()

