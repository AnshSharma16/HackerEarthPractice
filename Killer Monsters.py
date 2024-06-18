def count_and_remove_smaller_than_last(battlefield):
    if not battlefield:
        return 0  

    last_element = battlefield[-1]
    battlefield[:] = [monster for monster in battlefield if monster > last_element]
    battlefield.append(last_element) 
    return len(battlefield)

t = int(input())
for _ in range(t):
    n = int(input())
    strength = list(map(int, input().strip().split()))
    battlefield = []
    remaining = []
    
    for i in range(n):
        battlefield.append(strength[i])
        count = count_and_remove_smaller_than_last(battlefield)
        remaining.append(count)
    
    print(" ".join(map(str, remaining)))
