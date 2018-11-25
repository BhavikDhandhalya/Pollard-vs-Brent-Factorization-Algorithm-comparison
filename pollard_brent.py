"""
Bhavik Dhandhalya
BITS Pilani, ME Computer Science batch 2020
"""
from fractions import gcd
from random import randint
import time

def f(x, c, n):
    return (x ** 2 + c) % n

def pollards(n):  ##returns factor, count
    x = 2
    c = 1
    y = f(x, c, n)
    d = 1
    counter = 0

    found = False
    while not found:
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        d = gcd(abs(x - y), n)
        counter += 1

        if (d != 1 and d != n):
            found = True

        if (counter > 100000):
            return (-1, -1)
    print("N = %s g = %s rootg = %s steps = %s" % (n, d, round(pow(d,0.5),2), counter))

def brent(N):
    if N % 2 == 0:
        return 2
    step = 0
    y, c, m = randint(1, N - 1), randint(1, N - 1), randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y**2) % N + c) % N
        k = 0
        while (k < r and g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y**2) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            step+=1
            k = k + m
        r = r * 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            step += 1
            if g > 1:
                break
    print("N = %s g = %s rootg = %s steps = %s" % (N, g, round(pow(g,0.5),2), step))

    return g

print ("Pollard's result")
start_time = time.time()
pollards(10858954410599476117)
pollards(1147018434034049)
pollards(104681 * 104681)
pollards(104717 * 104717)
pollards(104729 * 104729)
pollards(104729 * 104717)
print ("--------------------------")
time1 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))

print ("Brent's result")
start_time = time.time()
brent(10858954410599476117)
brent(1147018434034049)
brent(104681 * 104681)
brent(104717 * 104717)
brent(104729 * 104729)
brent(104729 * 104717)
print ("--------------------------")
time2 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))

if time2 < time1:
    percent = (abs(time1 - time2))/time2
    print ("Brent is %s percent faster than pollard" % (round((percent*100), 2)))
else:
    percent = (abs(time2 - time1))/time1
    print ("Pollard is %s percent faster than brent" % (round((percent*100), 2)))
