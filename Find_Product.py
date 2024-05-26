n=int(input())
p=1
ele= list(map(int, input().split(" ")))  
for i in ele:
    p=i*p;
print(p)
