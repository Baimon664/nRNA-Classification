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
    
