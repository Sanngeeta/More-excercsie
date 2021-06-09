
list1=["hello","teak"]
list2=["dear","sir"]
i=0
y=[]
while i<len(list1):
    a=0
    while a<len(list2):
        k=list1[i],list2[a]
        y.append(k)
        a=a+1        
    i=i+1    
print(y)     
    