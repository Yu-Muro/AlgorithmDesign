# -*- coding: utf-8 -*-

vertex = 16  # 頂点数
unused = {k:k for k in range(vertex)}
used ={}
adjacent = [[0 for k in range(vertex)] for k in range(vertex)]
edges = [(4,0,1), (2,0,3), (3,0,6), (2,1,2), (7,1,4), (3,1,5),
(5,2,3), (2,2,5), (8,3,7), (5,4,5), (6,4,10), (8,4,12), (9,4,14), (3,5,8), (9,5,10), (5,6,7), (4,6,8), (7,6,9), (1,7,9), (8,7,11), (4,8,10), (4,9,10), (4,10,11), (7,10,13), (2,11,13), (8,12,13), (9,12,15), (4,13,14), (8,13,15), (3,14,15)]
cost = [[float('inf') for k in range(vertex)] for j in range(vertex)]
for edge in edges: # コスト行列の生成
   cost[edge[1]][edge[2]] = cost[edge[2]][edge[1]] = edge[0]
used[0] = unused.pop(0)


while len(unused) != 0:
   mini = int(1e3)
   m, n = -1, -1
   for i in used: # コスト最小を探す
      for j in unused:
         if mini > cost[i][j]:
            mini = cost[i][j]
            m, n = i, j
   unused.pop(n) # 削除
   used[n] = m
   adjacent[m][n] = 1


for k in range( vertex-1 ):
   for n in range( k+1, vertex ):
      if adjacent[k][n]==1:
         print( k, '-', n )