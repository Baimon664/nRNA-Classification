src_path = "fa/"
dst_path = "fa_scrape_2/"
name=open("fa/name.txt","r")
for i in name.readlines():
    i=i.strip()
    f = open("fa/"+i,'r')
    p="".join(f.readlines())
    if(p.count("\n") > 200):
        k=open(dst_path+i,"w")
        k.write(p)
        k.close()
    f.close()
name.close()