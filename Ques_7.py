list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
y=[]
i=0
while i<len(list1):
    k=list1[i]
    if k in list2:
        y.append(k)
    i=i+1
print(y)         