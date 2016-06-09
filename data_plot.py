#!/usr/bin/env python

import matplotlib.pyplot as plt


with open('data.txt', 'r') as infile:

	for line in infile:
		Concentration = line.split ( '[' )[ 0 ]
		survival = line.split ( '[' )[ 1 ].strip( ']\n' ).split(',' )


		svalues_list = []

		for value in survival:
			svalues_list.append( float(value))


		dots=[svalues_list]
		y = [Concentration]

		plt.plot( y, dots, 'ro')
		plt.axis([ -1, 20, 0, 190])
		plt.xlabel('Retinal Concentration')
		plt.ylabel('Survival in minutes')

	#plt.show()

	plt.savefig( 'data_plot.png' )
