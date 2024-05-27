s = input()
n = len(s)


unique_chars = ""
for i in range(n):
    char = s[i]
    if char not in unique_chars: 

        unique_chars += char  

print(unique_chars)

