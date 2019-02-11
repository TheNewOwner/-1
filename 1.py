def sumIntervals(list):
    num=0
    used=[]
    for items in list:
        for i in range(items[0],items[1]):
            if i not in used:
                used.append(i)
                num+=1
    return num
sumIntervals( [[1,2], [6, 10], [11, 15] ] )
sumIntervals( [[1,4], [7, 10], [3, 5] ] )
sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] )
            
            
        
            
    
