n=int(input())
p=1
ele= list(map(int, input().split(" "))) 
for i in ele:
  # Perform modulo operation at each step to prevent overflow
  p = (p * i) % (10**9 + 7) 
print(p)
