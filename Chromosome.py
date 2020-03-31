from random import randint, seed

'''
    Reprezentarea cromozomilor : liniara discreta ne-binara intreaga de tip permutare
'''


def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.problParam = problParam  # problParam has to store the number of nodes/cities
        self.repres = generateARandomPermutation(self.problParam['noNodes'])
        self.fitness = 0.0


    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.problParam['noNodes'] - 1)
        pos2 = randint(-1, self.problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.repres[pos1: pos2]
        for el in c.repres[pos2:] + c.repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.problParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.problParam['noNodes'] - 1)
        pos2 = randint(0, self.problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.repres[pos2]
        del self.repres[pos2]
        self.repres.insert(pos1 + 1, el)

    def __str__(self):
        return "\nChromo: " + str(self.repres) + " has fit: " + str(self.fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.repres == c.repres and self.fitness == c.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness