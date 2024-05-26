n=int(input())
s=0
ele= list(map(int, input().split(" ")))  
for i in ele:
    s=i+s;
print(s)
