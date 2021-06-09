a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
c=int(input("Enter the third no:"))
if a<b<c :
    print(c,"greater no")
elif c<b<a:
    print(a,"greater no")
elif b<a<c:
    print(c,"greater no")
elif c<a<b:
    print(b,"greater no") 
elif c<b<a:
    print(a,"greater no")
elif a<b<c:
    print(c,"greater no")    
else:
    print("all are equal")    