no = int(input())
l = []
d = 2
while(no > 1):
    while (no%d == 0):
        l.append(d)
        no /= d
    d += 1
print(max(l))
