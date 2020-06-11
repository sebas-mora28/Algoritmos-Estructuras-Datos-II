import random
import sys
import operator


"""
CODIGO OBTENIDO DE : https://github.com/Pantzan/KnapsackGA
"""


class Knapsack(object):	

    
	def __init__(self):	

		self.C = 0
		self.weights = []
		self.profits = []
		self.opt = []
		self.parents = []
		self.newparents = []
		self.bests = []
		self.best_p = [] 
		self.iterated = 1
		self.population = 0

    
		iMaxStackSize = 15000
		sys.setrecursionlimit(iMaxStackSize)




	"""Primeramente se crea la población inicial, la cual serán  arrays de tamaño 5, que contedrán valores random entre 0 y 1. Es decir es una población que se crea con características aleatorias
        """
	def initialize(self):

		for i in range(self.population):
			parent = []
			for k in range(0, 5):
				k = random.randint(0, 1)
				parent.append(k)
			self.parents.append(parent)

	def properties(self, weights, profits, opt, C, population):

		self.weights = weights
		self.profits = profits
		self.opt = opt
		self.C = C
		self.population = population
		self.initialize()




	"""
            Este método verifica el peso y la ganancia de cada array y con base a esto optiene el fitness de cada array evaluado. 
        """
	def fitness(self, item):

		sum_w = 0
		sum_p = 0

		for index, i in enumerate(item):
			if i == 0:
				continue
			else:
				sum_w += self.weights[index]
				sum_p += self.profits[index]

    
		if sum_w > self.C:
			return -1
		else: 
			return sum_p

		    




	def evaluation(self):

		
		best_pop = self.population // 2
		for i in range(len(self.parents)):
			parent = self.parents[i]
			ft = self.fitness(parent)
			self.bests.append((ft, parent))

	
		self.bests.sort(key=operator.itemgetter(0), reverse=True)
		self.best_p = self.bests[:best_pop]
		self.best_p = [x[1] for x in self.best_p]



	"""
            Este método se encarga de randorizar los arrays para obtener optimizar el proceso. Se podría decir que recrea la posibilidad de que un individuos sufra cambios de manera al azar parecido a como puede
            ocurrir en la naturaleza 
        """

	def mutation(self, ch):

		for i in range(len(ch)):		
			k = random.uniform(0, 1)
			if k > 0.5:
				
				if ch[i] == 1:
					ch[i] = 0
				else: 
					ch[i] = 1
		return ch



        """
            Este método combina las características de dos padres para obtener nos nuevos individuos hijos. 
        """
	def crossover(self, ch1, ch2):

		threshold = random.randint(1, len(ch1)-1)
		tmp1 = ch1[threshold:]
		tmp2 = ch2[threshold:]
		ch1 = ch1[:threshold]
		ch2 = ch2[:threshold]
		ch1.extend(tmp2)
		ch2.extend(tmp1)

		return ch1, ch2

	
	def run(self):

		self.evaluation()
		newparents = []
		pop = len(self.best_p)-1

		
		sample = random.sample(range(pop), pop)
		for i in range(0, pop):
			
			if i < pop-1:
				r1 = self.best_p[i]
				r2 = self.best_p[i+1]
				nchild1, nchild2 = self.crossover(r1, r2)
				newparents.append(nchild1)
				newparents.append(nchild2)
			else:
				r1 = self.best_p[i]
				r2 = self.best_p[0]
				nchild1, nchild2 = self.crossover(r1, r2)
				newparents.append(nchild1)
				newparents.append(nchild2)

		for i in range(len(newparents)):
			newparents[i] = self.mutation(newparents[i])

		if self.opt in newparents:
			print ("optimal found in {} generations" .format(self.iterated))
		else:
			self.iterated += 1
			print("recreate generations for {} time" .format(self.iterated))
			self.parents = newparents
			self.bests = []
			self.best_p = []
			self.run()	



"""
Cuando el algoritmo se inicializa con una población total de 100 por ejemplo, escoge 50 con el mejor fitness. En cada iteración se descartan aquellos individuos cuyo fitness es más bajo, además se combina entre ellos para
obtener nuevos individuos hijos con caracteristicas diferentes. También se realiza un proceso llamado mutacion en el cual de randoriza los arrays para obtener nuevas combinacion, sin embargo no es seguro pues si no se cumple la
condicion en ningun momento se realizará un cambio. Este proceso recrea la situacion de que un individuo puede sufrir mutaciones.

El algoritmo se obtiene hasta que se genera la generación óptima, de otra manera seguirá creando hijos. En este caso la solución óptima es [0,1,1,1,0]

"""
weights = [12,  7, 11, 8, 9]
profits = [24, 13, 23, 15, 16]
opt     = [0, 1, 1, 1, 0]
C = 26
population = 


k = Knapsack()
k.properties(weights, profits, opt, C, population)
k.run()
