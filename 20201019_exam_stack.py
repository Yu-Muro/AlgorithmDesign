N = 60
INF = float('inf')
depth = { k:INF for k in range( N ) }
edges = ((  0,  1 ), (  0, 10 ), (  1,  2 ), (  1, 11 ), (  2,  3 ), (  3,  4 ), (  4, 14 ), (  5,  6 ), (  5, 15 ), (  6, 16 ), (  7,  8 ), (  8, 18 ), (  9, 19 ), ( 10, 20 ), ( 11, 12 ), ( 12, 22 ), ( 13, 14 ), ( 15, 25 ), ( 16, 17 ), ( 17, 18 ), ( 18, 19 ), ( 20, 21 ), ( 21, 31 ), ( 22, 23 ), ( 24, 25 ), ( 24, 34 ), ( 25, 35 ), ( 26, 27 ), ( 26, 36 ), ( 27, 28 ), ( 28, 29 ), ( 28, 38 ), ( 30, 40 ), ( 31, 41 ), ( 32, 33 ), ( 33, 43 ), ( 34, 44 ), ( 35, 36 ), ( 35, 45 ), ( 36, 37 ), ( 37, 47 ), ( 38, 48 ), ( 39, 49 ), ( 40, 41 ), ( 40, 50 ), ( 42, 52 ), ( 43, 44 ), ( 44, 54 ), ( 45, 55 ), ( 46, 56 ), ( 47, 57 ), ( 48, 49 ), ( 48, 58 ), ( 49, 59 ), ( 50, 51 ), ( 51, 52 ), ( 52, 53 ), ( 53, 54 ), ( 56, 57 ))
nodes = { k :[] for k in range( N ) }
for edge in edges:
   nodes[edge[0]].append( edge[1] )
   nodes[edge[1]].append( edge[0] )
route = {k :k for k in range(N)}

start = 0
destination = 59
depth[start] = 0
visited =[]
stack = [start]   # for DFS
while route[destination] == destination:
   n = stack.pop()
   visited.append(n)
   depth[n] = len(stack)
   for i in nodes[n]:
      if i not in visited:
         stack.append(i)
         route[i] = n

t = destination
print(t, end = " ")
stack = [t]
while t != 0:
   print(route[t], end = " ")
   stack.append(t)
   t = route[t]
print("depth={}".format(len(stack)-1))