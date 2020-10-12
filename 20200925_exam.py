# -*- coding: utf-8 -*-
import random
import time

num = int(1e4)
x = random.sample( range(num), num )
start = time.time()





elapsed_time = time.time() - start
print( elapsed_time , 'sec' )
print( 'Max:', x[0], ' Mid:', x[int(num/2)], ' Min:', x[num-1] )
