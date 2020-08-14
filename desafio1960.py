algs =  {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
n = int(input())
rom = ''
m = s = 0
while True:
    for i in algs.keys():
        s = n - i
        if s < 0:
            break
        else:
            m = i
    s = n - m
    rom += algs[m]
    n = s
    #print(rom)
    if n <= 0:
        break
print(rom)
        
