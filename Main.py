from Citire import Citire
from GA import GA

def main():

    marimePopulatie = 100;
    nrGeneratii = 300;
    citire = Citire("hardE.txt")
    # graf = citire.citire()
    graf = citire.citireBerlin()
    ga = GA(marimePopulatie, graf)
    ga.initialisation()

    stop = False
    g = -1  # nr de generatii
    while not stop and g < 300:
        g = g + 1
        ga.oneGeneration()
        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))

main()
