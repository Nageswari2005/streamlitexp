n=10
even=[]
for i in range(n):
    if i%2==0:
        even.append(i)
odd=[x for x in range(n) if x%2==1]