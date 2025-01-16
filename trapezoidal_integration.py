def trapezoidal(x0, xk, dx, f):
    
    N = int((xk - x0) / dx)
    area = 0
    for i in range(1, N):
        area += f(x0 + i * dx)
    area = (dx / 2) * (f(x0) + f(xk) + 2 * area)
    
    return area  