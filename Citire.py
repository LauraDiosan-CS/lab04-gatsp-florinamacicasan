import math


class Citire:
    def __init__(self, numeFisier):
        self.__numeFisier = numeFisier

    '''
        Functie care citeste numarul de locatii (n) si durata parcurgerii drumului dintre ele
    '''
    def citire(self):
        net = {}
        try:
            f = open(self.__numeFisier, "r")
        except IOError:
            # file not exist
            print("Fisier inexistent !")

        nr = f.readline()
        n = int(nr)
        net['noNodes'] = n
        ma = [] # matricea de adiaceta

        for i in range(n):
            ma.append([])
            linie = f.readline()
            elemente = linie.split(",")
            for j in range(n):
                ma[-1].append(int(elemente[j]))

        net['mat'] = ma
        degrees = []
        noEdges = 0
        for i in range(n):
            d = 0
            for j in range(n):
                if ma[i][j] == 1:
                    d = d + 1
                if j > i:
                    noEdges = noEdges + ma[i][j]
            degrees.append(d)

        net['noEdges'] = noEdges
        net['degrees'] = degrees

        f.close()

        return net

    def dist(self, x1, x2, y1, y2):
        return round(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))

    def citire2(self):
        n = 51
        tpl = []
        with open(self.__numeFisier, "r") as f:
            for linie in range(n):
                nod, x, y = f.readline().split(" ")
                tpl.append((int(float(nod)), int(float(x)), int(float(y))))

        matrice = [[0 for _ in range(n)] for _ in range(n)]
        for pct1 in tpl:
            for pct2 in tpl:
                matrice[pct1[0] - 1][pct2[0] - 1] = self.dist(pct1[1], pct2[1], pct1[2], pct2[2])
                matrice[pct1[0] - 1][pct2[0] - 1] = self.dist(pct1[1], pct2[1], pct1[2], pct2[2])
        return matrice

    def citireBerlin(self):
        f = open(self.__numeFisier, "r")
        net = {}
        distante = self.citire2()
        net['mat'] = distante
        n = len(distante)
        net['noNodes'] = n
        f.close()
        return net