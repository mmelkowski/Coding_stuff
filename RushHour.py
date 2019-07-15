# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:17:16 2019

@author: mmelkowski
"""
import random
# Question: Faut il courrir dans les transports?

"""
Sur un trajet le temps d'une station à une autre est une constante le seul
moyen d'accelerer est d'arriver à attraper le metro d'avant.

les parametres sont donc le temps d'attentes entre metro et le nombre
de correspondances

En arrivant à une station le temps d'attente est de:

0 à 2 minutes en heure de pointe
0 à 4 minutes en temps normal
0 à 8 sur les lignes moins deservies
0 à 15 minutes sur la ligne 7

on admet que se presser fait gagner:

0.5 min si correspondance courte
1 min si correspondance longue


La logique est que le temps gagner en se pressant n'est uniquement gagné
que s'il n'est pas perdu à attendre.

Se presser pour obtenir le metro est aussi un gain

Ainsi il faut soit se presser pour obtenir le metro d'avant ou pour ne pas rater celui qui arrive


"""


class RailTime():
    def __init__(self, l_temps_metro, l_gain):
        # temps d'attente du metro
        self.l_temps_metro = l_temps_metro
        self.l_temps_attentes = [random.uniform(0, elt) for elt in l_temps_metro]
        self.l_gain = l_gain
        self.metro_evite = 0

    def calc_normal(self):
        """
        calcul du cas normal
        """
        self.temps_normal = sum(self.l_temps_attentes)

    def calc_presse(self):
        all_t = []
        i = 0
        while i < len(self.l_temps_metro):
            t_total = self.l_temps_metro[i]
            t_attente = self.l_temps_attentes[i]
            gain = self.l_gain[i]

            if gain + t_attente > t_total:
                t = 0
                self.metro_evite += 1
            else:
                t = t_attente
            all_t.append(t)
            i += 1

        self.temps_presse = sum(all_t)

    def worth_it():
        """
        Est ce que ça vaut le coup de se presser?
        """

    def pprint(self):
        print("Normal", round(self.temps_normal, 2))
        print("Pressé", round(self.temps_presse, 2))


if __name__ == "__main__":
    val = []
    val_p = []
    metro = []
    for _ in range(10000):
        rail = RailTime([10, 10], [2, 2])
        rail.calc_normal()
        val.append(rail.temps_normal)

        rail.calc_presse()
        val_p.append(rail.temps_presse)
        metro.append(rail.metro_evite)
    print(sum(val)/10000)
    print(sum(val_p)/10000)
    print(sum(metro)/10000)
    c = [metro.count(0), metro.count(1), metro.count(2)]
    c2 = [round((elt/10000)*100, 1) for elt in c]
    print(c2)
    
    