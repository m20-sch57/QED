from deflib.QED.xy_and_tu import t_u


def vec_a(x, y):
    t, u = t_u(x, y)

    if t < 0 or u < 0:
        return ([], (0, 0))

    A = [[(0, 0)] * (u + 1) for i in range(t + 1)]

    A[0][0] = (0, 1)

    for i in range(t + 1):
        for j in range(u + 1):
            if i != 0:
                A[i][j] = (A[i][j][0], A[i][j][1] - A[i - 1][j][0] + A[i - 1][j][1])
            if j != 0:
                A[i][j] = (A[i][j][0] + A[i][j - 1][0] + A[i][j - 1][1], A[i][j][1])

    return (A, A[t][u])


if __name__ == '__main__':
    x, y = map(int, input().split())
    A, a = vec_a(x, y)
    print(a)
    # print()
    # for arr in A:
    #     print(arr)
    # print()
    # t, u = t_u(x, y)
    # for i in range(t + 1):
    #     for j in range(u + 1):
    #         A[i][j] = rat(A[i][j][0] ** 2 + A[i][j][1] ** 2, 2 ** (i + j))
    # for arr in A:
    #     print(arr)
