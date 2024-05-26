test=int(input())
while(test!=0):
    n=int(input())
    s=input()
    odd=0
    for i in range(n):
       if(s.count(s[i])%2!=0):
           odd=odd+1
       else:
           odd=odd+0
    if(odd==0):
        print(0)
    else:
        print(odd-1)
    test=test-1
