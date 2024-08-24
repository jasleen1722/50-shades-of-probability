'''
Question: A drawer contains red socks and black socks. When socks are drawn at random,
the probability that both are red is 1/2. 
a) How small can the number of socks in the drawer be?
b) How small if the number of black socks is even?
'''

def sock_drawer():
    n = 3
    r = 2
    prob = 0
    while True:
        for r in range(2, r + 1):
            prob = (r/n) * ((r-1)/(n-1))
            if prob == 0.5:
                break
        if prob == 0.5:
            break
        r += 1
        n += 1
    return r, n

sock_drawer()