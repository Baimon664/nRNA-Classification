import tensorflow as tf
import numpy as np
from tensorflow import keras
import pandas as pd

x_test = np.load("3-mer_test.npy")
names=open("npy_2/name.txt",'r')
y=[]
y_e=[]
p=0
for i in names.readlines():
  q=[float(p)]*20
  y_e+=q
  p+=1
names.close()
y_test = np.array(y_e).reshape((19020,1)).astype("float32")
x_test = x_test.astype("float32")/4

model = keras.models.load_model("my_model_v7.h5")

names=open("npy_2/name.txt",'r')
score = []
# score_text = open("score.txt",'w')
index = 0 
labels = []
for i in names.readlines():
  i = i.strip()
  labels.append(i[:-4])
  eval_score = model.evaluate(x=x_test[index:index+20],y=y_test[index:index+20])
  score.append([i[:-4],eval_score[1]])
  # score_text.write(str(i[:-4])+" "+str(eval_score[1])+"\n")
  index+=20
names.close()
# score_text.close()

df = pd.DataFrame(score,columns=["RFAM families", "Accuracy"])
df.to_csv("score.csv",index=False)
