import math
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    s=list(map(int,input().split()))
    l=math.lcm(x,y)
    a=(x*y)//l
    c=1
    for i in range(n):
        if a!=0:
            if i%a!=(s[i]-1)%a:
                c=0
                break
        else:
            c=0
    if c==1:
        print("Yes")
    else:
        print("no")
