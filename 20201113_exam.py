# -*- coding: utf-8 -*-
def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

objects =[ ('1', 1), ('6', 6), ('9', 9), ('36', 36), ('81', 81 ), ('216', 216), ('729', 729), ('1296', 1296) ]
quiz = [14, 50, 71, 146, 245]

for q in quiz:
    tmp6, tmp9 = sum(list(map(int, base_10_to_n(q, 6)))), sum(list(map(int, base_10_to_n(q, 9))))
    if tmp6 < tmp9:
        print(tmp6)
    else:
        print(tmp9)