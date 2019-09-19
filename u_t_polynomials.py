from deflib import interpolation_polynom, rat
from QED.QED3 import vec_a

y = int(input())

with open("Data\\QED_poly_x_t.txt", 'w', encoding='utf-8') as outfile_x_t, \
        open("Data\\All_Data\\QED_poly_x_t_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_x_t_extra, \
        open("Data\\QED_poly_y_t.txt", 'w', encoding='utf-8') as outfile_y_t, \
        open("Data\\All_Data\\QED_poly_y_t_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_y_t_extra, \
        open("Data\\QED_poly_x_u.txt", 'w', encoding='utf-8') as outfile_x_u, \
        open("Data\\All_Data\\QED_poly_x_u_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_x_u_extra, \
        open("Data\\QED_poly_y_u.txt", 'w', encoding='utf-8') as outfile_y_u, \
        open("Data\\All_Data\\QED_poly_y_u_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_y_u_extra:
    A_tu = vec_a(1, y)[0]
    A_tu_x = [[A_tu[i][j][0] for j in range(len(A_tu[i]))] for i in range(len(A_tu))]
    A_tu_y = [[A_tu[i][j][1] for j in range(len(A_tu[i]))] for i in range(len(A_tu))]
    A_ut = [[A_tu[i][j] for i in range(len(A_tu))] for j in range(len(A_tu[0]))]
    A_ut_x = [[A_ut[i][j][0] for j in range(len(A_ut[i]))] for i in range(len(A_ut))]
    A_ut_y = [[A_ut[i][j][1] for j in range(len(A_ut[i]))] for i in range(len(A_ut))]

    P_x_t = [interpolation_polynom(list(range(1, len(A_tu_x[i]))), A_tu_x[i][1:], field=rat) for i in range(len(A_tu))]
    P_y_t = [interpolation_polynom(list(range(1, len(A_tu_y[i]))), A_tu_y[i][1:], field=rat) for i in range(len(A_tu))]
    P_x_u = [interpolation_polynom(list(range(1, len(A_ut_x[i]))), A_ut_x[i][1:], field=rat) for i in range(len(A_tu))]
    P_y_u = [interpolation_polynom(list(range(1, len(A_ut_y[i]))), A_ut_y[i][1:], field=rat) for i in range(len(A_tu))]

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
