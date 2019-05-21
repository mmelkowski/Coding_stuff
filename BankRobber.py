# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:32:55 2019

@author: mmelkowski
"""

"""
Banque a N coffre fort

Coffre fort a un code à C char allant de 0 à D

coffre traité dans l'ordre
1sec par combinaison
"""
class Banque():
    def __init__(self, list_coffre, list_voleur):
        self.coffres = []
        self.voleurs = []
        
        if list_coffre:
            for elt in list_coffre:
                self.add_coffre(elt[0], elt[1], elt[2])
        
        if list_voleur:
            for elt in list_voleur:
                self.add_voleur(elt)

    def add_coffre(self, C, D, color):
        self.coffres.append(Coffre(C, D, color))
    
    def add_voleur(self, color):
        self.voleurs.append(Voleur(color))
    
    def max_time_voleur(self):
        return max([elt.temps for elt in self.voleurs])
    
    def index_min_time_voleur(self):
        l_temps = [elt.temps for elt in self.voleurs]
        return l_temps.index(min(l_temps))
    
    def pick_coffre(self,color):
        l_coffre = [elt for elt in self.coffres if elt.color == color]
        if l_coffre:
            coffre = l_coffre[0]
            self.coffres.remove(coffre)
            return coffre
        return self.coffres.pop(0)
        
    
    def launch_heist(self):
        while self.coffres:
            # choose voleur pref
            index_voleur = self.index_min_time_voleur()
            pref = self.voleurs[index_voleur].pref
            coffre = self.pick_coffre(pref)
            self.voleurs[index_voleur].temps += coffre.time_to_unlock
        
        print(self.max_time_voleur(),"sec")


class Coffre():
    def __init__(self, C, D, color):
        self.character = C
        self.span = D
        self.time_to_unlock = D**C
        # couleur bleu (B) ou rouge (R)
        self.color = color


class Voleur():
    def __init__(self, color):
        self.temps = 0
        # couleur bleu (B) ou rouge (R)
        self.pref = color


if __name__ == "__main__":
    test = [[(2,5,"B"),(1,5,"R"),(3,5,"B"),(1,5,"R"),(1,5,"R")],
            ["R","B"]]
    
    import itertools
    l_combi_voleur = []
    for i in range(5):
        l_combi_voleur += list(itertools.product(["R", "B"], repeat=i))
    

    for elt in l_combi_voleur[1:]:
        print(elt)
        b = Banque(test[0], elt)
        b.launch_heist()



# BACKUP
"""
class Banque():
    def __init__(self, list_coffre, nb_voleur=0):
        self.coffres = []
        self.voleurs = []
        
        if list_coffre:
            for elt in list_coffre:
                self.add_coffre(elt[0], elt[1])
        
        if nb_voleur:
            self.add_voleur(nb_voleur)
        
        

    def add_coffre(self, C, D):
        self.coffres.append(Coffre(C, D, color))
    
    def add_voleur(self, nb):
        for _ in range(nb):
            self.voleurs.append(Voleur())
    
    def max_time_voleur(self):
        return max([elt.temps for elt in self.voleurs])
    
    def index_min_time_voleur(self):
        l_temps = [elt.temps for elt in self.voleurs]
        return l_temps.index(min(l_temps))
    
    def launch_heist(self):
        for coffre in self.coffres:
            self.voleurs[self.index_min_time_voleur()].temps += coffre.time_to_unlock
        print(self.max_time_voleur(),"sec")


class Coffre():
    def __init__(self, C, D, color):
        self.character = C
        self.span = D
        self.time_to_unlock = D**C
        # couleur bleu (B) ou rouge (R)
        self.color = color


class Voleur():
    def __init__(self):
        self.temps = 0
        # couleur bleu (B) ou rouge (R)
        self.pref = ""


if __name__ == "__main__":

    test_1 = [[(1,5)],1]
    test_2 = [[(2,5)],1]
    test_3 = [[(2,5),(1,5)],2]
    test_4 = [[(2,5),(1,5),(2,5)],2]
    test_5 = [[(2,5),(1,5),(3,5),(1,5),(1,5)],2]
    for elt in [test_1, test_2, test_3, test_4, test_5]:
        b = Banque(elt[0], nb_voleur=elt[1])
        b.launch_heist()
    """

    