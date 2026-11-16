import math

def q_solve(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        return "no real solution"
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2



print(q_solve(1, -5, 6))
