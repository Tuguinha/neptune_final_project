#!/usr/bin/env python

#From sample

import random


Retinal = [ 0, 5, 10, 15, 20 ] 
for Concentration in Retinal:
	print ( Concentration )


my_randoms=[]    

for i in range (30):    
    my_randoms.append(random.randrange(1,181))  
print (my_randoms) 
