n=int(input())
if n==0:
    print('[]')
elif n==1:
    l=[0]
    print(l)
else:
    l=[0,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    print(l)
   
        
