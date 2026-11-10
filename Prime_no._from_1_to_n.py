n=int(input("Enter number for prime number:"))

for i in range(2,n+1):
    for t in range(2,i):
        if i%t==0:
            break
    else:
        print(i)
