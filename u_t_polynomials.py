from deflib import interpolation_polynomial, Rational, DynamicMultiDimCoordList as DMDCL
from deflib.QED import B_table
from itertools import product

s = int(input())

with open("Data\\QED_poly_x_t.txt", 'w', encoding='utf-8') as outfile_x_t, \
     open("Data\\All_Data\\QED_poly_x_t_" + str(s) + ".txt", 'w', encoding='utf-8') as outfile_x_t_extra, \
     open("Data\\QED_poly_y_t.txt", 'w', encoding='utf-8') as outfile_y_t, \
     open("Data\\All_Data\\QED_poly_y_t_" + str(s) + ".txt", 'w', encoding='utf-8') as outfile_y_t_extra, \
     open("Data\\QED_poly_x_u.txt", 'w', encoding='utf-8') as outfile_x_u, \
     open("Data\\All_Data\\QED_poly_x_u_" + str(s) + ".txt", 'w', encoding='utf-8') as outfile_x_u_extra, \
     open("Data\\QED_poly_y_u.txt", 'w', encoding='utf-8') as outfile_y_u, \
     open("Data\\All_Data\\QED_poly_y_u_" + str(s) + ".txt", 'w', encoding='utf-8') as outfile_y_u_extra:
    A = B_table({(s + 1, s + 1)}, mass=1)
    A_x = DMDCL(2)
    A_y = DMDCL(2)
    for i, j in product(range(s + 2), range(s + 2)):
        A_x[i, j] = A[i, j][0]
        A_y[i, j] = A[i, j][1]

    P_x_t = [interpolation_polynomial(list(range(1, s + 2)), list(A_x[i, 1:i + 1, None]), field=Rational) for i in range(s + 1)]
    P_y_t = [interpolation_polynomial(list(range(1, s + 2)), list(A_y[i, 1:i + 1, None]), field=Rational) for i in range(s + 1)]
    P_x_u = [interpolation_polynomial(list(range(1, s + 2)), list(A_x[1, i:None, i + 1]), field=Rational) for i in range(s + 1)]
    P_y_u = [interpolation_polynomial(list(range(1, s + 2)), list(A_y[1, i:None, i + 1]), field=Rational) for i in range(s + 1)]

    for pol in P_x_t:
        print(*pol.coefficients, '\n', file=outfile_x_t)
        print(*pol.coefficients, '\n', file=outfile_x_t_extra)
    for pol in P_y_t:
        print(*pol.coefficients, '\n', file=outfile_y_t)
        print(*pol.coefficients, '\n', file=outfile_y_t_extra)
    for pol in P_x_u:
        print(*pol.coefficients, '\n', file=outfile_x_u)
        print(*pol.coefficients, '\n', file=outfile_x_u_extra)
    for pol in P_y_u:
        print(*pol.coefficients, '\n', file=outfile_y_u)
        print(*pol.coefficients, '\n', file=outfile_y_u_extra)
