#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       electre.py
#       
#       Copyright 2011 Fco Javier Lucena <fran.lucena@gmail.com>
#       
#       ReglajesF1 is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       ReglajesF1 is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with ReglajesF1; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from Math import sqrt

class Electre:
	
	def __init__ (self,alternativas, atributos):
		self.alternativas = alternativas
		self.atributos = atributos
		self.pesos = [0] * atributos
		self.optimo = [0] * atributos
		self.decisional = [[0] * atributos] * alternativas
		self.normalizada = [[0] * atributos] * alternativas
		self.ponderada = [[0] * atributos] * alternativas
		self.concordada = [[0] * atributos] * alternativas
		self.discordada = [[0] * atributos] * alternativas
		self.dominancia = [[0] * atributos] * alternativas
		
		
	def establecerPesos(self, prioridad):
		
		total = 0.0
		for i in range(0, self.atributos):
			total += prioridad[i]
		for i in range(0, self.atributos):
			self.pesos[i] = prioridad[i]
		
	def establecerOptimo(self, optimo):
		
		for i in range(0, self.atributos):
			self.optimo[i] = optimo[i]
					
	def __establecerDecisional(self, decisional):
		
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				self.decisional[i][j] = decisional[i][j]		
	
	def establecerNormalizada(self):
		
		for j in range(0, self.atributos):
			suma = 0
			for i in range(0, self.alternativas):
				cuadrado = self.decisional[i][j] * self.decisional[i][j]
				suma = suma + cuadrado
			
			suma = sqrt(suma)
			for i in range(0, self.alternativas):
				self.normalizada[i][j] = (self.decisional[i][j] / suma)
			
	
	def establecerPonderada(self):
		
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				self.ponderada[i][j] = self.normalizada[i][j] * self.pesos[j]
				
	def establecerConcordada(self):
		print ""
	
	def establecerDiscordada(self):
		print ""
	
	def establecerDominada(self):
		print ""
	
	def resolver(self, decisional, prioridad, optimo):
		
		self.establecerPesos(prioridad)
		self.establecerOptimo(optimo)
		self.establecerDecisional(decisional)
		self.establecerNormalizada()
		self.establecerPonderada()
		self.establecerConcordada()
		self.establecerConcordada()
		self.establecerDominada()
		
	def mostrar(self, matriz):
		
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				print matriz[i][j],
			print			
