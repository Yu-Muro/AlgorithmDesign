def MergeSort( List ) :
   if len( List ) < 2:
      return List

   i=len( List )//2
   x=MergeSort( List[:i] )
   y=MergeSort( List[i:] )
   m=[]

   while x!=[] and y!=[]:
      if x[0] < y[0]:
         m.append(y.pop(0))
      else:
         m.append(x.pop(0))
   if x != []:
      m.extend(x)
   if y != []:
      m.extend(y)

   return m

A = [ 11, 7, 10, 4, 2, 8, 1, 9, 5, 3, 6 ]
print('Befor :', A )
A = MergeSort( A )
print('After :', A )
