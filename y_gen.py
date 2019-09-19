from QED.QED3 import vec_a

with open("QED_y.txt", 'w', encoding='utf-8') as outfile:
    y = int(input())
    A = vec_a(1, 2 * y - 1)[0]

    Y = [A[t][y - t - 1] for t in range(y)]

    L = 0
    L_x = 0
    L_y = 0
    L_sum = 0
    for i in range(len(Y)):
        pair = tuple(map(str, Y[i] + (Y[i][0] + Y[i][1],)))
        Y[i] = pair
        L = max(L, len(pair[0]), len(pair[1]))
        L_x = max(L_x, len(pair[0]))
        L_y = max(L_y, len(pair[1]))
        L_sum = max(L_sum, len(pair[2]))

    for i in range(len(Y)):
        outfile.write('(' + Y[i][0] + ' ' * (L - len(Y[i][0])) + ', ' + Y[i][1] + ' ' * (L - len(Y[i][1])) + ')   ')
    outfile.write('\n\n')
    for i in range(len(Y)):
        outfile.write('(' + Y[i][0] + ' ' * (L_x - len(Y[i][0])) + ')   ')
    outfile.write('\n\n')
    for i in range(len(Y)):
        outfile.write('(' + Y[i][1] + ' ' * (L_y - len(Y[i][1])) + ')   ')
    outfile.write('\n\n')
    for i in range(len(Y)):
        outfile.write('(' + Y[i][2] + ' ' * (L_sum - len(Y[i][2])) + ')   ')
    outfile.write('\n\n')
    print(sum(list(map(lambda pair: int(pair[0]), Y[0: -(y//2) - 1]))) - sum(list(map(lambda pair: int(pair[0]), Y[-(y//2): -1]))), file = outfile)