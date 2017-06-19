#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#def calcula(line):
'''
if line=='0':
	return 0
if line=='1':
	return 1
'''
#print line
for line in sys.stdin:
	#print "ENTRADA:",
	#print line,
	resultado=0
	potencia=2
	indice=len(line)-2
	#print "ÍNDICEBASE:",
	#print indice
	for i in line:
		#print "CARACTER:",
		#print i,
		if i=='1':
			#print "RESULTADO:",
			resultado+=(potencia**indice)
			#print resultado
			#print "ÍNDICE1:",
			indice=indice-1
			#print indice
		if i=='0':
			#print "ÍNDICE0:",
			indice=indice-1
			#print indice
	#print "SAÍDA:",
	print resultado
	#return resultado
		#print



'''for line in sys.stdin:
	print "ENTRADA",
	print line
	print "SAÍDA:",
	print calcula(line)
	#print line,
	#print len(line)-1
	#bin=int(line)
	#print bin'''