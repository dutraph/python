def fat(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

for i in range(10): 
    print(f' Fatorial de {i}: {fat(i)}')