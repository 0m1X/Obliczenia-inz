def simpson(x0, xk, dx, f):

    sum_bound = 0
    sum_center = 0
    N = int((xk - x0) / dx)

    for i in range(1, N):
        x = x0 + i * dx
        if i % 2 == 0:
            sum_bound += f(x)
        else:
            sum_center += f(x)

    area = dx / 3 * (f(x0) + f(xk) + 2 * sum_bound + 4 * sum_center)    
    
    return area
