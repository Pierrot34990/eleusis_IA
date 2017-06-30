from math import *
import json

class Joueur:

    #nombre de cartes dans une main jouée
    lotDe1 = 0
    lotDe2 = 0
    lotDe3 = 0
    lotDe4 = 0
    lotDe5 = 0

    #variables concernant un lot
    simple = 0          #une carte pareil
    double = 0          #deux cartes pareils...
    triple = 0
    quadruple = 0
    suiteCroissante = 0
    suiteDecroissante = 0
    couleur1sur2 = 0    #une rouge puis une noir ou inversement
    memeCouleur = 0

    #Variables concernant une carte d'un lot
    rouge = 0
    noir = 0
    pair = 0
    impaire = 0
    trefles = 0
    coeur = 0
    piques = 0
    carreau = 0
    un = 0
    deux = 0
    trois = 0
    quatre = 0
    cinq = 0
    six = 0
    sept = 0
    huit = 0
    neuf = 0
    dix = 0
    onze = 0        #vallet
    douze = 0       #dame
    treize = 0      #roi

    #Variables concernant les cartes de deux lots distincts
    #carteSup = 0        #carte N+1 > carte N
    #carteInf = 0        #carte N+1 < carte N
    #couleurDif = 0     #couleur N+1 != couleur N
    #couleurPareil = 0  #couleur N+1 = couleur N
    #figureDif = 0       #trefle, coeur, pique, carreau N+1 != figure N
    #figurePareil = 0    #trefle, coeur, pique, carreau N+1 = figure N
    somme = 0
    valSomme = 0
    ancSomme = 0
    valAncSomme = 0
    sommeCarte = [somme, valSomme, ancSomme, valAncSomme]

    #sous-tableaux de score
    scoreNbCartes = [lotDe1,lotDe2,lotDe3,lotDe4, lotDe5]
    scoreUnLot = [simple, double, triple, quadruple, suiteCroissante, suiteDecroissante, couleur1sur2, memeCouleur]
    scoreCartes = [rouge, noir, pair, impaire, trefles, coeur, piques, carreau, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize]

    #scoreSuiteLots = [carteSup, carteInf, couleurDif, couleurPareil, figureDif, figurePareil, sommeCarte]

    #tableau final
    score = [scoreNbCartes, scoreUnLot, scoreCartes]#,scoreSuiteLots]

    def jouerCartes(self, detailsPartie):
        partie = json.loads(detailsPartie)
        self.analyseBonneCartes(partie['bonnes-cartes'])
        self.analyseMauvaiseCartes(partie['mauvaises-cartes'])
        cartes = self.choisirCartes()
        if cartes == None:
            return 'prophete'
        return cartes

    def analyseBonneCartes(self, lotsDeCartes):
        premierLot = 1
        for lot in lotsDeCartes:
            self.calculScoreNbCartes(lot, '+')    #score du nb de carte dans un lot joue
            self.calculScoreUnLot(lot, '+')           #score du tableau scoreUnLot
            for carte in lot:
                self.calculScoreRougeNoir(carte, '+')    #score du tableau scoreCarte
                self.calculScoreParite(carte, '+')
                self.calculScoreFigure(carte, '+')
                self.calculScoreNumero(carte, '+')
            if premierLot == 1:
                premierLot = 0
                ancienLot = lot
            else:
                self.calculScoreSommeNumero(lot, ancienLot, '+') #pas encore commencer
                ancienLot = lot



    def analyseMauvaiseCartes(self, lotsDeCartes):
        premierLot = 1
        for lot in lotsDeCartes:
            self.calculScoreNbCartes(lot, '-')    #score du nb de carte dans un lot joue
            self.calculScoreUnLot(lot, '-')           #score du tableau scoreUnLot
            for carte in lot:
                self.calculScoreRougeNoir(carte, '-')    #score du tableau scoreCarte
                self.calculScoreParite(carte, '-')
                self.calculScoreFigure(carte, '-')
                self.calculScoreNumero(carte, '-')
            if premierLot == 1:
                premierLot = 0
                ancienLot = lot
            else:
                self.calculScoreSommeNumero(lot, ancienLot, '-')
                ancienLot = lot



    def choisirCartes(self):
        return



    def calculScoreRougeNoir(self, carte, sens):
        if (carte['color'] == 'D') or (carte['color'] == 'H'):
            if sens == '+':
                self.scoreCartes[0] += 1
            elif sens == '-':
                self.scoreCartes[0] -= 1
        elif (carte['color'] == 'C') or (carte['color'] == 'S'):
            if sens == '+':
                self.scoreCartes[1] += 1
            elif sens == '-':
                self.scoreCartes[1] -= 1



    def calculScoreParite(self, carte, sens):
        if (carte['number'] % 2) == 0:
            if sens == '+':
                self.scoreCartes[2] += 1
            elif sens == '-':
                self.scoreCartes[2] -= 1
        elif (carte['number'] % 2) == 1:
            if sens == '+':
                self.scoreCartes[3] += 1
            elif sens == '-':
                self.scoreCartes[3] -= 1



    def calculScoreFigure(self, carte, sens):
        if carte['color'] == 'C':
            if sens == '+':
                self.scoreCartes[4] += 1
            elif sens == '-':
                self.scoreCartes[4] -= 1
        elif carte['color'] == 'H':
            if sens == '+':
                self.scoreCartes[5] += 1
            elif sens == '-':
                self.scoreCartes[5] -= 1
        elif carte['color'] == 'S':
            if sens == '+':
                self.scoreCartes[6] += 1
            elif sens == '-':
                self.scoreCartes[6] -= 1
        elif carte['color'] == 'D':
            if sens == '+':
                self.scoreCartes[7] += 1
            elif sens == '-':
                self.scoreCartes[7] -= 1



    def calculScoreNumero(self, carte, sens):
        if carte['number'] == 1:
            if sens == '+':
                self.scoreCartes[8] += 1
            elif sens == '-':
                self.scoreCartes[8] -= 1
        elif carte['number'] == 2:
            if sens == '+':
                self.scoreCartes[9] += 1
            elif sens == '-':
                self.scoreCartes[9] -= 1
        elif carte['number'] == 3:
            if sens == '+':
                self.scoreCartes[10] += 1
            elif sens == '-':
                self.scoreCartes[10] -= 1
        elif carte['number'] == 4:
            if sens == '+':
                self.scoreCartes[11] += 1
            elif sens == '-':
                self.scoreCartes[11] -= 1
        elif carte['number'] == 5:
            if sens == '+':
                self.scoreCartes[12] += 1
            elif sens == '-':
                self.scoreCartes[12] -= 1
        elif carte['number'] == 6:
            if sens == '+':
                self.scoreCartes[13] += 1
            elif sens == '-':
                self.scoreCartes[13] -= 1
        elif carte['number'] == 7:
            if sens == '+':
                self.scoreCartes[14] += 1
            elif sens == '-':
                self.scoreCartes[14] -= 1
        elif carte['number'] == 8:
            if sens == '+':
                self.scoreCartes[15] += 1
            elif sens == '-':
                self.scoreCartes[15] -= 1
        elif carte['number'] == 9:
            if sens == '+':
                self.scoreCartes[16] += 1
            elif sens == '-':
                self.scoreCartes[16] -= 1
        elif carte['number'] == 10:
            if sens == '+':
                self.scoreCartes[17] += 1
            elif sens == '-':
                self.scoreCartes[17] -= 1
        elif carte['number'] == 11:
            if sens == '+':
                self.scoreCartes[18] += 1
            elif sens == '-':
                self.scoreCartes[18] -= 1
        elif carte['number'] == 12:
            if sens == '+':
                self.scoreCartes[19] += 1
            elif sens == '-':
                self.scoreCartes[19] -= 1
        elif carte['number'] == 13:
            if sens == '+':
                self.scoreCartes[20] += 1
            elif sens == '-':
                self.scoreCartes[20] -= 1




    def calculScoreNbCartes(self, lot, sens):
        nbCarte = len(lot)
        if nbCarte == 1:
            if sens == '+':
                self.scoreNbCartes[0] += 1
            elif sens == '-':
                self.scoreNbCartes[0] -= 1
        elif nbCarte == 2:
            if sens == '+':
                self.scoreNbCartes[1] += 1
            elif sens == '-':
                self.scoreNbCartes[1] -= 1
        elif nbCarte == 3:
            if sens == '+':
                self.scoreNbCartes[2] += 1
            elif sens == '-':
                self.scoreNbCartes[2] -= 1
        elif nbCarte == 4:
            if sens == '+':
                self.scoreNbCartes[3] += 1
            elif sens == '-':
                self.scoreNbCartes[3] -= 1
        elif nbCarte == 5:
            if sens == '+':
                self.scoreNbCartes[4] += 1
            elif sens == '-':
                self.scoreNbCartes[4] -= 1



    def calculScoreUnLot(self, lot, sens):
        self.calculScoreCarteIdentique(lot, sens)
        self.calculScoreSuite(lot, sens)
        self.calculScoreCouleur(lot, sens)



    #Determine si un double, triple... doit etre joue
    def calculScoreCarteIdentique(self, lot, sens):
        compteur = 1
        premiereCarte = 1
        ancienneCarte = 0
        for carte in lot:
            if premiereCarte == 1:
                premiereCarte = 0
                ancienneCarte = carte
            else:
                if carte['number'] == ancienneCarte['number']:
                    compteur += 1
                ancienneCarte == carte
        if compteur == 1:
            if sens == '+':
                self.scoreUnLot[0] += 1
            elif sens == '-':
                self.scoreUnLot[0] -= 1
        elif compteur == 2:
            if sens == '+':
                self.scoreUnLot[1] += 1
            elif sens == '-':
                self.scoreUnLot[1] -= 1
        elif compteur == 3:
            if sens == '+':
                self.scoreUnLot[2] += 1
            elif sens == '-':
                self.scoreUnLot[2] -= 1
        elif compteur == 4:
            if sens == '+':
                self.scoreUnLot[3] += 1
            elif sens == '-':
                self.scoreUnLot[3] -= 1



    def calculScoreSuite(self, lot, sens):
        suiteCroissante = 1
        suiteDecroissante = 1
        premiereCarte = 1
        ancienneCarte = 0
        for carte in lot:
            if premiereCarte == 1:
                premiereCarte = 0
                ancienneCarte = carte
            else:
                if carte['number'] < ancienneCarte['number']:
                    suiteCroissante = 0
                elif carte['number'] > ancienneCarte['number']:
                    suiteDecroissante = 0
                ancienneCarte == carte
        if suiteCroissante == 1:
            if sens == '+':
                self.scoreUnLot[4] += 1
            elif sens == '-':
                self.scoreUnLot[4] -= 1
        if suiteDecroissante == 1:
            if sens == '+':
                self.scoreUnLot[5] += 1
            elif sens == '-':
                self.scoreUnLot[5] -= 1


    def calculScoreCouleur(self, lot, sens):
        couleurDifferente = 1
        memeCouleur = 1
        premiereCarte = 1
        ancienneCouleur = 0
        couleur = 0
        for carte in lot:
            if premiereCarte == 1:
                premiereCarte = 0
                if (carte['color'] == 'D') or (carte['color'] == 'H'):
                    ancienneCouleur = 'rouge'
                elif (carte['color'] == 'C') or (carte['color'] == 'S'):
                    ancienneCouleur = 'noir'
            else:
                if (carte['color'] == 'D') or (carte['color'] == 'H'):
                    couleur = 'rouge'
                elif (carte['color'] == 'C') or (carte['color'] == 'S'):
                    couleur = 'noir'
                if couleur != ancienneCouleur:
                    memeCouleur = 0
                elif couleur == ancienneCouleur:
                    couleurDifferente = 0
            if couleurDifferente == 1:
                if sens == '+':
                    self.scoreUnLot[6] += 1
                elif sens == '-':
                    self.scoreUnLot[6] -= 1
            if memeCouleur == 1:
                if sens == '+':
                    self.scoreUnLot[7] += 1
                elif sens == '-':
                    self.scoreUnLot[7] -= 1

    def calculScoreSommeNumero(self, lot, ancienLot, sens):
        total = 0
        totalAncien = 0
        for carte in lot:
            total += carte['number']
        for carte in ancienLot:
            totalAncien += carte['number']
        if total == totalAncien:
            if self.sommeCarte[0] == total:
                if sens == '+':
                    self.sommeCarte[1] += 1
                elif sens == '-':
                    self.sommeCarte[1] -= 1
            else:
                if sens == '+':
                    self.sommeCarte[1] = 1
                elif sens == '-':
                    self.sommeCarte[1] = -1
            self.sommeCarte[0] = total
        if self.sommeCarte[1] > self.sommeCarte[3]:
            self.sommeCarte[3] = self.sommeCarte[1]
            self.sommeCarte[2] = self.sommeCarte[0]
