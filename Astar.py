
class Node:
    def __init__(self, listeadjac):
        self.listeadjac = listeadjac

    def voisin(self, f):
        return self.listeadjac[f]
    
    def heuris(self, n):
        H = {'A': 10,'B': 5,'C': 5,'D': 10,'E':10,'F':3,'G':3,'H':3,'I':0,}
        return H[n]

    def etoile(self, ndepart, narrive):
        louverte = set([ndepart])
        lferme = set([])

        G = {}

        G[ndepart] = 0

        prede = {}
        prede[ndepart] = ndepart
        ##################

        while len(louverte) > 0:
            n = None

            for f in louverte:
                if n == None or G[f] + self.heuris(f) < G[n] + self.heuris(n):
                    n = f;

            if n == None:
                print('chemin nexiste pas')
                return None
            ################
            
            if n == narrive:
                chemin = []

                while prede[n] != n:
                    chemin.append(n)
                    n = prede[n]
                    
                    

                chemin.append(ndepart)

                chemin.reverse()

                print('le chemin est {}'.format(chemin))
                return chemin
            ##################################

            for (m, weight) in self.voisin(n):
                
                if m not in louverte and m not in lferme:
                    louverte.add(m)
                    prede[m] = n
                    G[m] = G[n] + weight

                else:
                    if G[m] > G[n] + weight:
                        G[m] = G[n] + weight
                        prede[m] = n

                        if m in lferme:
                            lferme.remove(m)
                            louverte.add(m)

            louverte.remove(n)
            lferme.add(n)

        print('chemin nexiste pas')
        return None
listeadjac = {'D': [('A', 5), ('E',2 ),('C',6)],'A': [('C', 5)],'E': [('B', 5)],'C':[('H',3),('F',2),('B',3)],'B':[('C', 3), ('E', 5), ('F', 3), ('G', 4),
('I', 5)],'F':[('G', 3), ('B', 3), ('C', 2)],'H':[('C', 3), ('I', 4)],'I':[('H', 4), ('G', 3), ('B', 5)],
'G':[('B', 4), ('F', 3), ('I', 3)],}
graph = Node(listeadjac)
graph.etoile('A', 'I')
