from math import factorial
from deflib.QED.xy_and_tu import t_u


def binomial(n, k):
    if type(n) != int or type(k) != int:
        raise TypeError('Binomial coefficient only for non-negative integers')
    if n < 0 or k < 0:
        return 0
    if n < k:
        return 0
    return factorial(n) // factorial(k) // factorial(n-k)


def vec_a(x, y):
    t, u = t_u(x, y)

    if u != 0 and t != 0:
        a_x = sum([binomial(t, 2 * k) * binomial(u - 1, 2 * k)
                   - binomial(t, 2 * k + 1) * binomial(u - 1, 2 * k + 1) for k in range(min((u - 1) // 2, t // 2) + 1)])

        a_y = sum([binomial(t, 2 * k + 2) * binomial(u - 1, 2 * k + 1)
                   - binomial(t, 2 * k + 1) * binomial(u - 1, 2 * k) for k in range(0, min((u - 1) // 2, (t - 1) // 2) + 1)])

        return (a_x, a_y)

    if u == 0:
        return (0, 1)

    if t == 0:
        return (1, 0)