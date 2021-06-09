 
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
y=[]
while i<len(list1):
    k=list1[i]
    if k is not list2:
        y.append(k)
       
    i=i+1    
print(y)        

        

