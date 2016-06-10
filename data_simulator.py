#!/usr/bin/env python

#random sample generation for retinal concentration

import random
#import numpy as np


outfile = open( "data.txt","w" )


data = [ ]  
Retinal = [ 0, 5, 10, 15 ] 


for Concentration in Retinal:

	data = random.sample( range( 0, 181 ), 31 )
	

	#print ( "{} {}\n".format( Concentration, data ))

		
	outfile.write( "{} {}\n".format( Concentration, data ))

outfile.close()