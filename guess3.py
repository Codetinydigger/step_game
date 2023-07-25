n=int(input("What is the value of range: "))
k=int(input("What is the value of iteration: "))
a=pow(2,k)
b=n/a
c=n-b
print("Eliminated: "+str(c))
print("Remaining: "+str(b))