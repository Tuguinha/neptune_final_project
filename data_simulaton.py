#!/usr/bin/env python

#random sample generation for retinal concentration

import random
import numpy as np
import matplotlib.pyplot as plt


outfile = open("test.txt","w")


my_randoms=[]  

Retinal = [ 0, 5, 10, 15 ] 


dots=[]
y=[]


for Concentration in Retinal:

	my_randoms=random.sample(range(0, 181), 31)
	dots.append(my_randoms)
	y.append([Concentration]*30)
	
		
	outfile.write( "{} {}\n".format(Concentration, my_randoms))

outfile.close()