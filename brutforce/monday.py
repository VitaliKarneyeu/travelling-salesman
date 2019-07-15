#!/usr/bin/python3

# Monday

p = [[500, 124, 141, 141, 148, 144, 140, 129, 121, 23, 137, 139],
     [23, 500, 21, 22, 28, 22, 21, 13, 11, 12, 16, 17],
     [47, 25, 500, 15, 11, 27, 24, 19, 22, 18, 20, 21],
     [38, 24, 8, 500, 15, 23, 20, 18, 21, 17, 16, 17],
     [42, 30, 15, 15, 500, 27, 24, 22, 27, 24, 20, 21],
     [43, 23, 27, 26, 38, 500, 5, 18, 21, 17, 12, 11],
     [42, 23, 23, 22, 32, 5, 500, 17, 21, 17, 10, 11],
     [27, 15, 14, 16, 20, 15, 15, 500, 13, 8, 9, 10],
     [26, 14, 22, 23, 29, 23, 22, 14, 500, 5, 17, 18],
     [22, 9, 21, 22, 28, 22, 21, 12, 105, 500, 16, 16],
     [37, 18, 19, 19, 30, 8, 7, 13, 17, 13, 500, 7],
     [34, 15, 16, 16, 25, 13, 12, 12, 14, 10, 7, 500]]

shops = [
    "0 Home",
    "1 Belarus Zhilunovicha 4",
    "2 petrovski Bachilo 14",
    "3 prostor Partizanski 182",
    "4 Sosedi selickogo 65",
    "5 rublevski nesterova 58",
    "6 Evroopt Nesterova 49",
    "7 Belmarket Varvasheni 1",
    "8 Vitalur partizanski 106",
    "9 ZRPT Partizanski 107",
    "10 Baikalski Angarskaja 38/2",
    "11 ZRPT Angarskaja 10"]

best_len = 88888888888888
best_route = []
not_used = list(range(12))

for i0 in range(1, 12):
    not_used0 = not_used[:]
    if i0 not in not_used0:
        continue
    not_used0.remove(i0)
    for i1 in range(1, 12):
        not_used1 = not_used0[:]
        if i1 not in not_used1:
            continue
        not_used1.remove(i1)
        for i2 in range(1, 12):
            not_used2 = not_used1[:]
            if i2 not in not_used2:
                continue
            not_used2.remove(i2)
            for i3 in range(1, 12):
                not_used3 = not_used2[:]
                if i3 not in not_used3:
                    continue
                not_used3.remove(i3)
                for i4 in range(1, 12):
                    not_used4 = not_used3[:]
                    if i4 not in not_used4:
                        continue
                    not_used4.remove(i4)
                    for i5 in range(1, 12):
                        not_used5 = not_used4[:]
                        if i5 not in not_used5:
                            continue
                        not_used5.remove(i5)
                        for i6 in range(1, 12):
                            not_used6 = not_used5[:]
                            if i6 not in not_used6:
                                continue
                            not_used6.remove(i6)
                            for i7 in range(1, 12):
                                not_used7 = not_used6[:]
                                if i7 not in not_used7:
                                    continue
                                not_used7.remove(i7)
                                for i8 in range(1, 12):
                                    not_used8 = not_used7[:]
                                    if i8 not in not_used8:
                                        continue
                                    not_used8.remove(i8)
                                    for i9 in range(1, 12):
                                        not_used9 = not_used8[:]
                                        if i9 not in not_used9:
                                            continue
                                        not_used9.remove(i9)
                                        for i10 in range(1, 12):
                                            not_used10 = not_used9[:]
                                            if i10 not in not_used10:
                                                continue
                                            route_len = (p[0][i0] + p[i0][i1] + p[i1][i2] + p[i2][i3] + p[i3][i4] +
                                                         p[i4][i5] + p[i5][i6] + p[i6][i7] + p[i7][i8] + p[i8][i9] +
                                                         p[i9][i10] + p[i10][0])
                                            if route_len < best_len:
                                                best_route = [shops[0], shops[i0], shops[i1], shops[i2], shops[i3],
                                                              shops[i4], shops[i5], shops[i6], shops[i7], shops[i8],
                                                              shops[i9], shops[i10], shops[0]]
                                                best_len = route_len
                                                print(best_len, best_route)
                                                print("routes", p[0][i0], p[i0][i1], p[i1][i2], p[i2][i3], p[i3][i4],
                                                      p[i4][i5], p[i5][i6], p[i6][i7], p[i7][i8], p[i8][i9],
                                                      p[i9][i10], p[i10][0])
