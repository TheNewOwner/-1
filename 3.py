f = open("code.txt","r")
lines = f.readlines()
f.close()
f = open("code.txt","w")
af=0
cline=""
da=0
sec=1
lim=0
lin=0
for line in lines:
    if "#" not in line:
        f.write(line)
    else:
        for i in range(0,len(line)):
            if line[i]=='\"' and af==0:
                af=1
                lim=1
            if line[i]=='\"' and af==1 and lim==0:
                af=0
                sec=1
            if line[i]=="#" and af==1:
                cline=cline+line[i]
                sec=0
                lin=1
            if line[i]=="#" and af==0:
                da=1
            if da==0:
                if sec==0:
                    pass
                else:
                    cline=cline+line[i]
            lim=0
        if lin==1:
            if "\n" not in cline:
                cline=cline+"\n"
        lin=0
        f.write(cline)
        cline=""
        da=0
        sec=1
f.close()
