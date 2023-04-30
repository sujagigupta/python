n=int(input("enter the no. greater than 7:"))
for i in range(n):
    if i==2 or i==n-3:
        print("#"*n)
    else:
        print(" "*2,"#"," "*(n-6),"#",sep="")
