# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. Jaise:



string= ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0
y=[]
while i<len(string):
    k=string[i]
    if k not in y:
        y.append(k)
    i=i+1
print(y)        



string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 
i=0
n=[]
while i<len(string_list):
    k=string_list[i]
    if k not in n:
        n.append(k)
    i=i+1
print(n)        