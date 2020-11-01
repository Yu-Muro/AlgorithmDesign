# -*- coding: utf-8 -*-
edges =[(1,11), (1,12), (1,14), (2,12), (2,14), (3,11), (3,12), (3,13), (4,13), (4,15), (5,12), (5,14), (6,11), (6,15), (7,13), (7,14), (7,15), (8,12), (8,13), (8,15), (9,14), (9,15), (10,11), (10,15)]

v2 = {k: [] for k in range(15, 10, -1)}
for edge in edges:
    v2[edge[1]].append(edge[0])
for k in v2:
    v2[k].sort(reverse = True)
v1_use = {k: 0 for k in range(10, 0, -1)}
v2_use = {k: 0 for k in range(15, 10, -1)}
pair_list = []
print("v2", v2)

min_edges = 4
while min(v2_use.values()) != 4:
    check_list = []
    for k in v2:
        if len(v2[k]) == min_edges:
            check_list.append(k)
    print("cl", check_list)
    check_list.sort(reverse = True)
    for k in check_list:
        tmp_pair = []
        sum, tmp_v1, tmp_v2 = 0, 0, 0
        for j in v2[k]:
            if v1_use[j] != 2 and v2_use[k] != 4:
                if sum < k + j:
                    if [k, j] not in pair_list:
                        print(k, j)
                        tmp_pair = [k, j]
                        sum = k + j
                        tmp_v1, tmp_v2 = j, k
        if tmp_pair == []:
            min_edges += 1
            break
        pair_list.append(tmp_pair)
        print(v1_use, v2_use, tmp_pair, pair_list, sep = "\n")
        input()
        v1_use[tmp_v1] += 1
        v2_use[tmp_v2] += 1
