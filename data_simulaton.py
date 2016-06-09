#!/usr/bin/env python

#random sample generation for retinal concentration

import random
import sys
import numpy as np
import matplotlib.pyplot as plt

#np.random.randn( 4, 5) #generating normal distribution sample


sys.stdout = open("test.txt","w")

my_randoms=[]  


Retinal = [ 0, 5, 10, 15 ] 

dots=[]
y=[]
for Concentration in Retinal:
	my_randoms=random.sample(range(0, 181), 31)
	dots.append(my_randoms)
	y.append([Concentration]*30)
	#for i in range (my_randoms ) :   
		#plt.plot(Concentration,[lines][i], 'ro')	
		#my_randoms.append(random.randrange( 0, 181 ))  #1 to 180 minutes and number of observations

	 
	print ( "Concentration {}: {} minutes survival".format(Concentration, my_randoms) )


#text_file = open("/home/s-mendes/repos/neptune_final_project", "r")

