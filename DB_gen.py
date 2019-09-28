from deflib.QED import B_table
from itertools import product

y = int(input())

with open("Data\\QED_vec_B.txt", 'w', encoding='utf-8') as outfile, \
        open("Data\\All_Data\\QED_vec_B_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_extra, \
        open("Data\\QED_vec_B_x.txt", 'w', encoding='utf-8') as outfile_x, \
        open("Data\\All_Data\\QED_vec_B_x_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_x_extra, \
        open("Data\\QED_vec_B_y.txt", 'w', encoding='utf-8') as outfile_y, \
        open("Data\\All_Data\\QED_vec_B_y_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_y_extra, \
        open("Data\\QED_vec_B_sum.txt", 'w', encoding='utf-8') as outfile_sum, \
        open("Data\\All_Data\\QED_vec_B_sum_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_sum_extra, \
        open("Data\\QED_Q.txt", "w", encoding='utf-8') as outfile_Q, \
        open("Data\\All_Data\\QED_Q_" + str(y) + ".txt", 'w', encoding='utf-8') as outfile_Q_extra:
    A = B_table({(y, y)})

    L = 0
    L_x = 0
    L_y = 0
    L_sum = 0
    L_P = 0

    # gen_values: (<\\vec{B}(i, j)[0]>,
    #              <\\vec{B}(i, j)[1]>,
    #              <\\vec{B}(i, j)[0] + \\vec{B}(i, j)[1]>,
    #              <Q(i, j)>)
    for i, j in product(range(A.sizes[0]), range(A.sizes[1])):
        gen_values = tuple(map(str, A[i, j] + (A[i, j][0] + A[i, j][1], A[i, j][0] ** 2 + A[i, j][1] ** 2)))
        A[i, j] = gen_values
        L = max(L, len(gen_values[0]), len(gen_values[1]))
        L_x = max(L_x, len(gen_values[0]))
        L_y = max(L_y, len(gen_values[1]))
        L_sum = max(L_sum, len(gen_values[2]))
        L_P = max(L_P, len(gen_values[3]))

    for i in range(A.sizes[0]):
        for j in range(A.sizes[1]):
            outfile.write('(' + A[i, j][0] + ' ' * (L - len(A[i, j][0])) + ', ' + A[i, j][1] + ' ' * (L - len(A[i, j][1])) + ')   ')
            outfile_extra.write('(' + A[i, j][0] + ' ' * (L - len(A[i, j][0])) + ', ' + A[i, j][1] + ' ' * (L - len(A[i, j][1])) + ')   ')
            outfile_x.write('(' + A[i, j][0] + ' ' * (L_x - len(A[i, j][0])) + ')   ')
            outfile_x_extra.write('(' + A[i, j][0] + ' ' * (L_x - len(A[i, j][0])) + ')   ')
            outfile_y.write('(' + A[i, j][1] + ' ' * (L_y - len(A[i, j][1])) + ')   ')
            outfile_y_extra.write('(' + A[i, j][1] + ' ' * (L_y - len(A[i, j][1])) + ')   ')
            outfile_sum.write('(' + A[i, j][2] + ' ' * (L_sum - len(A[i, j][2])) + ')   ')
            outfile_sum_extra.write('(' + A[i, j][2] + ' ' * (L_sum - len(A[i, j][2])) + ')   ')
            outfile_Q.write(A[i, j][3] + ' ' * (L_P - len(A[i, j][3]) + 2))
            outfile_Q_extra.write(A[i, j][3] + ' ' * (L_P - len(A[i, j][3]) + 2))
        outfile.write('\n\n')
        outfile_extra.write('\n\n')
        outfile_x.write('\n\n')
        outfile_x_extra.write('\n\n')
        outfile_y.write('\n\n')
        outfile_y_extra.write('\n\n')
        outfile_sum.write('\n\n')
        outfile_sum_extra.write('\n\n')
        outfile_Q.write('\n\n')
        outfile_Q_extra.write('\n\n')
