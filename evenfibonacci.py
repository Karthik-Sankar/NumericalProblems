#dynamic programming method
dpm = [0]*4000000
def fib(n):
    if(n<=1):
        return n;
    if(dpm[n] != 0):
        return dpm[n];
    else:
        dpm[n] = fib(n-1)+fib(n-2)
        return dpm[n]

fib(33)
dump = [x for x in dpm if x%2==0 and x!=0]
print(sum(dump))

