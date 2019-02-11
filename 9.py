def maxSequence(list):
    here1=min(list)
    here2=min(list)
    pinpoint1=0
    pinpoint2=0
    suma1=0
    suma2=0
    newlist=[]
    if max(list)>0:
        for i in range(0,len(list)):
            suma1 = suma1 + list[i]
            if suma1>here1:
                here1=suma1
                pinpoint1=i
        for j in range(pinpoint1,-1,-1):
            suma2 = suma2 + list[j]
            if suma2>here2:
                here2=suma2
                pinpoint2=j
        for r in range(pinpoint2,pinpoint1+1):
            newlist.append(list[r])
        return newlist
    else:
        newlist.append(max(list))
        return newlist
print maxSequence([-7,-3,-5,-4,-1,-3,-2,-5])
print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
