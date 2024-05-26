test = int(input())
while (test != 0):
    s = input()
    n = len(s)


    words = s.split()
    w = len(words)

    
    for i in range(w // 2): 
        words[i], words[w - i - 1] = words[w - i - 1], words[i]

    test = test - 1

    
    print(" ".join(words))
