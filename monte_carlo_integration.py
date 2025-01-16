import random as r

def monte_carlo(x0, xk, dx, f):

    N = int(dx)
    sum = 0

    for i in range(1, N):
        x = r.uniform(x0, xk)
        sum += f(x) 
    
    area = (xk - x0) * sum / N

    return area
