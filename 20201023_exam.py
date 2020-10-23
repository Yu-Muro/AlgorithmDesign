# -*- coding: utf-8 -*-
vertex = 16  # ノード数
edges = [(4,0,1), (2,0,3), (3,0,6), (2,1,2), (7,1,4), (3,1,5),
(5,2,3), (2,2,5), (8,3,7), (5,4,5), (6,4,10), (8,4,12), (9,4,14), (3,5,8), (9,5,10), (5,6,7), (4,6,8), (7,6,9), (1,7,9), (8,7,11), (4,8,10), (4,9,10), (4,10,11), (7,10,13), (2,11,13), (8,12,13), (9,12,15), (4,13,14), (8,13,15), (3,14,15)] #( cost, edge1, edge2 )
start = 0
destination = 15

visited = set()
vertex_cost = { k:[ float('inf'), k ] for k in range( vertex ) }
edge_cost = { k:{} for k in range( vertex ) }
for edge in edges:
   edge_cost[edge[1]][edge[2]] = edge_cost[edge[2]][edge[1]] = edge[0]

visited.add(start)
vertex_cost[start][0] = 0
while vertex_cost[destination][0] == float("inf"):
   next_node, pre_node, min_cost = 99, 99, int(1e3) # 初期化
   for node in visited:
      for i in edge_cost[node]:
         if edge_cost[node][i] + vertex_cost[node][0] < min_cost and i not in visited: # 最小コストを調べる
            min_cost = edge_cost[node][i] + vertex_cost[node][0]
            next_node = i
            pre_node = node
   visited.add(next_node)
   vertex_cost[next_node][0], vertex_cost[next_node][1] = min_cost, pre_node
route = [destination]
tmp = destination
while tmp != start:
   tmp = vertex_cost[tmp][1]
   route.append(tmp)
print("cost = {}, route = {}".format(vertex_cost[destination][0], route[::-1]))