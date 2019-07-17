#!/usr/bin/python3

# Friday

p = [[500, 143, 139, 41, 48, 31, 130, 134, 126, 39, 32, 32],
     [43, 500, 18, 18, 27, 37, 36, 44, 26, 46, 38, 38],
     [49, 16, 500, 9, 13, 37, 35, 43, 23, 43, 37, 37],
     [50, 14, 9, 500, 21, 38, 36, 44, 24, 43, 37, 37],
     [53, 28, 14, 21, 500, 42, 40, 47, 39, 47, 42, 42],
     [40, 35, 30, 30, 42, 500, 3, 12, 24, 12, 7, 7],
     [38, 34, 29, 34, 39, 3, 500, 12, 23, 12, 10, 9],
     [47, 42, 37, 42, 48, 16, 12, 500, 28, 23, 14, 14],
     [27, 24, 18, 18, 26, 23, 22, 28, 500, 42, 24, 24],
     [47, 43, 38, 41, 46, 12, 12, 23, 32, 500, 9, 9],
     [41, 37, 32, 31, 40, 7, 10, 14, 26, 9, 500, 1],
     [41, 37, 32, 31, 40, 7, 10, 14, 26, 9, 1, 500]]

shops = [
    "0 Home",
    "1 Belmarket M4 5-kilometr",
    "2 Krama52 Selickogo 107",
    "3 prostor Partizanski 182",
    "4 Sosedi selickogo 65",
    "5 rublevski nesterova 58",
    "6 Evroopt Nesterova 49",
    "7 Ohotski Ohotskaja 135/1",
    "8 Vitalur partizanski 106",
    "9 Rublevski Ilimskaya 27",
    "10 Belmarket Nesterova 94",
    "11 Zlatka Nesterova 94a"]

best_len = 88888888888888
best_route = []
not_used = list(range(12))

# for i0 in range(12):
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
