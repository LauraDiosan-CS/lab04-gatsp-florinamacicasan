import heapq
from random import randint
from Chromosome import Chromosome


class GA:
    def __init__(self, popSize=None, problParam=None):
        self.__popSize = popSize
        self.__problParam = problParam
        self.__population = []

    def initialisation(self):
        for _ in range(0, self.__popSize):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
        heapq.heapify(self.__population)

    def evaluation(self):
        matrice = self.__problParam['mat']
        for c in self.__population:
            distanta = 0
            for i in range(len(c.repres) - 1):
                distanta = distanta + matrice[c.repres[i]][c.repres[i+1]]
            distanta = distanta + matrice[c.repres[len(c.repres) - 1]][c.repres[0]]
            c.fitness = distanta


    def bestChromosome(self):
        return self.__population[0] #heap => cel mai bun va fi in varf

    def selection(self):
        pos1 = randint(0, self.__popSize - 1)
        pos2 = randint(0, self.__popSize - 1)
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def newPopulation(self):
        newPop = []
        for _ in range(self.__popSize - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            descendeti = p1.crossover(p2)
            descendeti.mutation()
            newPop.append(descendeti)

        heapq.heapify(newPop)
        return newPop

    def oneGeneration(self):
        newGen = self.newPopulation()
        newPop = []
        i = 0
        for i in range(int(self.__popSize/2)):
            newPop.append(self.__population[i])
        p = 0
        for j in range(i+1, self.__popSize):
            newPop.append(newGen[p])
            p = p + 1
        self.__population = newPop
        self.evaluation()
        heapq.heapify(self.__population)