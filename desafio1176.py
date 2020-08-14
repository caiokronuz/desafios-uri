def fb(n):
    fb = [0, 1]

    if n > 1:
        for i in range(2, n + 1):
            f = fb[i - 2] + fb[i - 1]
            fb.append(f)
            
    return fb[n]

c = int(input())

for x in range(c):
    n = int(input())
    f = fb(n)
    print('Fib({}) = {}'.format(n, f))
