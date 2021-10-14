import numpy as np
names=open("fa_scrape_2/name.txt",'r')
dst_path = "npy_2/"
for i in names.readlines():
    i=i.strip()
    n=0
    name = i
    file = open("fa_scrape_2/"+name,'r')
    data=[]
    for line in file:
        raw_data = line.strip()
        if len(raw_data) != 0 :
            if (raw_data[0] != '>' and len(raw_data) <= 200) :
               data.append(raw_data)
               n+=1
    file.close()
    if(n >= 100): 
        k=np.array(data)
        np.save(dst_path+name[:-3],k)
names.close()