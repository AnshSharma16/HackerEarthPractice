s=input()
n=len(s)
i=0
count=0
for i in range(n):
    if(s[i]==s[n-1-i]):
        count=count+1
    else:
        count=0
if(count==n):
    print("YES")
else:
    print("NO")
