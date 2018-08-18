import time
start_time = time.clock()
def ispalindrome(x):
    n = 0
    m = x
    while(m>0):
        n = (n*10)+(m%10)
        m = m//10
    return n==x
r = 0
##for p in range(990,99,-11):
##    for q in range(999,99,-1):
##        t = p*q
##        print(p,q,t)
##        if(r < t and ispalindrome(t)):
##            r = t;
##            break;
##        elif(t<r):
##            break;
s = 0
for p in range(999,100,-1):
    if(p%11==0):
        q=999
        s=1
    else:
        q = 990
        s = 11
    while(q>99):
        t = p*q
        if(r<t and ispalindrome(t)):
           r=t;
           break;
        q-=s
print(r)
print("Program took ", time.clock() - start_time, "Seconds to run")
#12.303788818399468 sec
