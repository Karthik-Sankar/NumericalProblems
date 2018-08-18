import time
st = time.clock()
##def mul_of_3_5(n):
##    s = 0
##    for i in range(1, n):
##        if(i%3==0 or i%5==0):
##            s += i
##    print(s)

def sumofdiv(n):
    t = 9999999
    p = t//n
    return n*((p*(p+1))//2)
##mul_of_3_5(10000000)
print(sumofdiv(3)+sumofdiv(5)-sumofdiv(15))
print(time.clock()-st)
