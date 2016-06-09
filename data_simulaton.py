#!/usr/bin/env python

#From sample

import random

my_randoms=[]  


Retinal = [ 0, 5, 10 ] 


for Concentration in Retinal:

	for i in range ( 1 ) :   
		my_randoms=random.sample(range(0, 181), 5)
		#my_randoms.append(random.randrange( 0, 181 ))  #1 to 180 minutes and number of observations

	 
	print ( "Concentration {}: {} minutes survival".format(Concentration, my_randoms) )

