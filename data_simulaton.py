#!/usr/bin/env python

#From sample

import random

my_randoms=[]  


Retinal = [ 0, 5, 10, 15, 20 ] 


for Concentration in Retinal:
	print ( "Concentration {}: {} minutes".format(Concentration, my_randoms) )


for i in range (30):    

    my_randoms.append(random.randrange(0,181))  #1 to 180 h
print (my_randoms) 




