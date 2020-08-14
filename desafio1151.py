n = int(input())
if n > 0 and n < 46:
    f1 = 0
    f2 = 1
    ft = [f1, f2]
    c = 2
    while c < n:
        f3 = f1 + f2
        ft.append(f3)
        f1 = f2
        f2 = f3
        c += 1
    for i in range(n):
        ft[i] = str(ft[i])

    ft = ' '.join(ft)
    print(ft)
