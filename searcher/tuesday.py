#!/usr/bin/python3

# Tuesday

p = [[500, 37, 141, 146, 40, 42, 158, 40, 46, 134],
     [41, 500, 15, 19, 18, 15, 22, 13, 24, 20],
     [42, 22, 500, 16, 15, 25, 31, 9, 14, 19],
     [40, 18, 19, 500, 1, 15, 31, 9, 6, 8],
     [41, 20, 19, 1, 500, 17, 33, 11, 8, 9],
     [41, 18, 30, 16, 17, 500, 30, 23, 18, 13],
     [66, 19, 28, 30, 29, 26, 500, 24, 36, 32],
     [44, 13, 12, 9, 8, 20, 26, 500, 13, 13],
     [46, 23, 17, 7, 7, 16, 36, 13, 500, 16],
     [31, 24, 19, 9, 10, 13, 38, 16, 19, 500]]

shops = [
    "1 Home",
    "2 posttorg16 Soltysa 189",
    "3 Evroopt Filimonova 13/1",
    "4 prod Dolgobrodskaya 11",
    "5 Posttorg37 Dolgobrodskaja 10/1",
    "6 posstorg10 Scherbakova 29",
    "7 Belmarket Sviazistov 13",
    "8 Rublevski 2per Bagrationa 18a",
    "9 Posttorg6 Uralskaya 12",
    "10 Traktorozavodskoy Budennogo 16a"]

best_len = 88888888888888
best_route = []
not_used = list(range(10))

for i0 in range(1, 10):
    not_used0 = not_used[:]
    if i0 not in not_used0:
        continue
    not_used0.remove(i0)
    for i1 in range(1, 10):
        not_used1 = not_used0[:]
        if i1 not in not_used1:
            continue
        not_used1.remove(i1)
        for i2 in range(1, 10):
            not_used2 = not_used1[:]
            if i2 not in not_used2:
                continue
            not_used2.remove(i2)
            for i3 in range(1, 10):
                not_used3 = not_used2[:]
                if i3 not in not_used3:
                    continue
                not_used3.remove(i3)
                for i4 in range(1, 10):
                    not_used4 = not_used3[:]
                    if i4 not in not_used4:
                        continue
                    not_used4.remove(i4)
                    for i5 in range(1, 10):
                        not_used5 = not_used4[:]
                        if i5 not in not_used5:
                            continue
                        not_used5.remove(i5)
                        for i6 in range(1, 10):
                            not_used6 = not_used5[:]
                            if i6 not in not_used6:
                                continue
                            not_used6.remove(i6)
                            for i7 in range(1, 10):
                                not_used7 = not_used6[:]
                                if i7 not in not_used7:
                                    continue
                                not_used7.remove(i7)
                                for i8 in range(1, 10):
                                    not_used8 = not_used7[:]
                                    if i8 not in not_used8:
                                        continue
                                    route_len = (p[0][i0] + p[i0][i1] + p[i1][i2] + p[i2][i3] + p[i3][i4] +
                                                 p[i4][i5] + p[i5][i6] + p[i6][i7] + p[i7][i8] + p[i8][0])
                                    if route_len < best_len:
                                        best_route = [shops[0], shops[i0], shops[i1], shops[i2], shops[i3],
                                                      shops[i4], shops[i5], shops[i6], shops[i7], shops[i8],
                                                      shops[0]]
                                        best_len = route_len
                                        print(best_len, best_route)
                                        print("routes", p[0][i0], p[i0][i1], p[i1][i2], p[i2][i3], p[i3][i4],
                                              p[i4][i5], p[i5][i6], p[i6][i7], p[i7][i8], p[i8][0])
