f = open("code.txt","r")
lines = f.readlines()
f.close()
f = open("code.txt","w")
af=0
af1=0
cline=""
da=0
sec=1
lim=0
lin=0
for line in lines:
    if "#" not in line:
        f.write(line)
        print line
    elif line[0]=="#":
        pass
    else:
        for i in range(0,len(line)):
            if line[i]=='\"' and (af==0 and af1==0):
                af=1
                lim=1
            elif line[i]=="\'" and (af==0 and af1==0):
                af1=1
                lim=1
            if line[i]=='\"' and af==1 and lim==0 and af1==0:
                af=0
                sec=1
            elif line[i]=="\'" and af1==1 and lim==0 and af==0:
                af1=0
                sec=1
            if line[i]=="#" and (af==1 and af1==1):
                cline=cline+line[i]
                sec=0
            if line[i]=="#" and (af==0 and af1==0):
                da=1
            if da==0:
                if sec==0:
                    pass
                else:
                    cline=cline+line[i]
            lim=0
        if "\n" not in cline:
                cline=cline+"\n"
        lin=0
        f.write(cline)
        print cline
        cline=""
        da=0
        sec=1
f.close()
