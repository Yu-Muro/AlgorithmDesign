# -*- coding: utf-8 -*-
import random
import time
import matplotlib.pyplot as plt


def bubble_sort( x ):
    for i in range(num):
        for j in range(num-1-i):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


def selection_sort( x ):
    for k in range(num - 1):
        for j in range( k+1, num ):
            if x[k] < x[j]:
                x[k], x[j] = x[j], x[k]
    return x


def merge_sort( List ):
    if len( List ) < 2:
        return List

    i=len( List )//2
    x=merge_sort( List[:i] )
    y=merge_sort( List[i:] )
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

num = int(1e3)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
mergex = []
mergey = []
for i in range(10):
    x = random.sample( range(num), num )
    start = time.time()

    x = merge_sort( x )

    elapsed_time = time.time() - start
    mergex.append(num)
    mergey.append(elapsed_time)
    print( elapsed_time , 'sec' )
    print( 'Max:', x[0], ' Mid:', x[num//2], ' Min:', x[num-1] )
    num = int(1e4) * (i+1)
ax.plot(mergex, mergey, "-", marker = "o", color = "red", linestyle = "solid")

num = int(1e3)
selectx = []
selecty = []
for i in range(10):
    x = random.sample( range(num), num )
    start = time.time()

    x = selection_sort( x )
    elapsed_time = time.time() - start
    selectx.append(num)
    selecty.append(elapsed_time)
    print( elapsed_time , 'sec' )
    print( 'Max:', x[0], ' Mid:', x[num//2], ' Min:', x[num-1] )
    num += int(1e3)
ax.plot(selectx, selecty, "-", marker = "v", color = "blue", linestyle = "solid")

num = int(1e3)
bubblex = []
bubbley = []
for i in range(10):
    x = random.sample( range(num), num )
    start = time.time()

    x = bubble_sort( x )
    elapsed_time = time.time() - start
    bubblex.append(num)
    bubbley.append(elapsed_time)
    print( elapsed_time , 'sec' )
    print( 'Max:', x[0], ' Mid:', x[num//2], ' Min:', x[num-1] )
    num += int(1e3)
ax.plot(bubblex, bubbley, "-", marker = "x", color = "green", linestyle = "solid")

num = int(1e3)
methodx = []
methody = []
for i in range(10):
    x = random.sample( range(num), num )
    start = time.time()

    x.sort(reverse = True)
    elapsed_time = time.time() - start
    methodx.append(num)
    methody.append(elapsed_time)
    print( elapsed_time , 'sec' )
    print( 'Max:', x[0], ' Mid:', x[num//2], ' Min:', x[num-1] )
    num = int(1e4) * (i+1)
ax.plot(methodx, methody, "-", marker = "D", color = "magenta", linestyle = "solid")


ax.set_ylim(top = 5)
ax.set_title("Sort Time")
ax.set_xlabel("Number of data")
ax.set_ylabel("Time")
ax.legend(["MergeSort", "SelectionSort", "BubbleSort", "Method"])
ax.grid(True)
plt.show()