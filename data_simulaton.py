#!/usr/bin/env python

#random sample generation for retinal concentration

import random
import sys
import numpy as np

#np.random.randn( 4, 5)


#sys.stdout = open("test.ods","w")

my_randoms=[]  


Retinal = [ 0, 5, 10, 15 ] 


for Concentration in Retinal:

	for i in range ( 1 ) :   
		my_randoms=random.sample(range(0, 181), 31)
		#my_randoms.append(random.randrange( 0, 181 ))  #1 to 180 minutes and number of observations

	 
	print ( "Concentration {}: {} minutes survival".format(Concentration, my_randoms) )

#generating normal distribution sample

