# -*- coding:Utf8 -*-

from math import *
import json

class Joueur:

    premierTour = 1

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


#Variable main joueur
    # nombre de cartes dans une main jouée
    lotDe1Main = 0
    lotDe2Main = 0
    lotDe3Main = 0
    lotDe4Main = 0
    lotDe5Main = 0

    # variables concernant un lot
    simpleMain = 0  # une carte pareil
    doubleMain = 0  # deux cartes pareils...
    tripleMain = 0
    quadrupleMain = 0
    suiteCroissanteMain = 0
    suiteDecroissanteMain = 0
    couleur1sur2Main = 0  # une rouge puis une noir ou inversement
    memeCouleurMain = 0

    # Variables concernant une carte d'un lot
    rougeMain = 0
    noirMain = 0
    pairMain = 0
    impaireMain = 0
    treflesMain = 0
    coeurMain = 0
    piquesMain = 0
    carreauMain = 0
    unMain = 0
    deuxMain = 0
    troisMain = 0
    quatreMain = 0
    cinqMain = 0
    sixMain = 0
    septMain = 0
    huitMain = 0
    neufMain = 0
    dixMain = 0
    onzeMain = 0  # vallet
    douzeMain = 0  # dame
    treizeMain = 0  # roi

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
    sommeCarteJoue = [somme, valSomme, ancSomme, valAncSomme]

    #sous-tableaux de score des cartes jouées
    scoreNbCartesJoue = [lotDe1,lotDe2,lotDe3,lotDe4, lotDe5]
    scoreUnLotJoue = [simple, double, triple, quadruple, suiteCroissante, suiteDecroissante, couleur1sur2, memeCouleur]
    scoreCartesJoue = [rouge, noir, pair, impaire, trefles, coeur, piques, carreau, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize]

    # sous-tableaux de score des cartes dans ma main
    scoreNbCartesMain = [lotDe1Main, lotDe2Main, lotDe3Main, lotDe4Main, lotDe5Main]
    scoreUnLotMain = [simpleMain, doubleMain, tripleMain, quadrupleMain, suiteCroissanteMain, suiteDecroissanteMain, couleur1sur2Main, memeCouleurMain]
    scoreCartesMain = [rougeMain, noirMain, pairMain, impaireMain, treflesMain, coeurMain, piquesMain, carreauMain, unMain, deuxMain, troisMain, quatreMain, cinqMain, sixMain, septMain, huitMain, neufMain, dixMain, onzeMain, douzeMain, treizeMain]

    #scoreSuiteLots = [carteSup, carteInf, couleurDif, couleurPareil, figureDif, figurePareil, sommeCarte]

    #tableau final
    scoreJoue = [scoreNbCartesJoue, scoreUnLotJoue, scoreCartesJoue]#,scoreSuiteLots]

    def bonneCarte(self):
        cartes = [[{"color":"C","number":"2"},{"color":"S","number":"1"},{"color":"H","number":"8"}],[{"color":"H","number":"5"},{"color":"D","number":"10"}],[{"color":"S","number":"12"},{"color":"H","number":"11"},{"color":"D","number":"13"}],[{"color":"S","number":"6"},{"color":"D","number":"6"},{"color":"S","number":"6"}]]
        return cartes



    def mauvaiseCarte(self):
        cartes = [[{"color":"C","number":"3"},{"color":"D","number":"4"}],[{"color":"S","number":"9"}],[{"color":"S","number":"6"}],[{"color":"S","number":"9"}],[{"color":"C","number":"3"},{"color":"D","number":"4"}]]
        return cartes

    def main(self):
        return [{"color":"C","number":"3"},{"color":"D","number":"4"},{"color":"D","number":"4"},{"color":"S","number":"1"},{"color":"H","number":"8"}]

    def jouerCartes(self, detailsPartie):
        #partie = json.loads(detailsPartie)
        #self.analyseBonneCartes(partie['bonnes-cartes'])
        self.analyseBonneCartes(self.bonneCarte(), 0)
        #self.analyseMauvaiseCartes(partie['mauvaises-cartes'])
        self.analyseMauvaiseCartes(self.mauvaiseCarte(), 0)

        #cartes = self.choisirCartes(partie['deckJ1'])
        cartes = self.choisirCartes(self.main())
        if cartes == None:
            return 'prophete'
        return cartes

    def analyseBonneCartes(self, lotsDeCartes, joueur):
        premierLot = 1
        for lot in lotsDeCartes:
            self.calculScoreNbCartes(lot, '+', joueur)    #score du nb de carte dans un lot joue
            self.calculScoreUnLot(lot, '+', joueur)           #score du tableau scoreUnLot
            for carte in lot:
                self.calculScoreRougeNoir(carte, '+', joueur)    #score du tableau scoreCarte
                self.calculScoreParite(carte, '+', joueur)
                self.calculScoreFigure(carte, '+', joueur)
                self.calculScoreNumero(carte, '+', joueur)
            if premierLot == 1:
                premierLot = 0
                ancienLot = lot
            else:
                self.calculScoreSommeNumero(lot, ancienLot, '+', joueur) #pas encore commencer
                ancienLot = lot



    def analyseMauvaiseCartes(self, lotsDeCartes, joueur):
        premierLot = 1
        for lot in lotsDeCartes:
            self.calculScoreNbCartes(lot, '-', joueur)    #score du nb de carte dans un lot joue
            self.calculScoreUnLot(lot, '-', joueur)           #score du tableau scoreUnLot
            for carte in lot:
                self.calculScoreRougeNoir(carte, '-', joueur)    #score du tableau scoreCarte
                self.calculScoreParite(carte, '-', joueur)
                self.calculScoreFigure(carte, '-', joueur)
                self.calculScoreNumero(carte, '-', joueur)
            if premierLot == 1:
                premierLot = 0
                ancienLot = lot
            else:
                self.calculScoreSommeNumero(lot, ancienLot, '-', joueur)
                ancienLot = lot



    def choisirCartes(self, cartes):
        main = [cartes]
        if self.premierTour == 1:
            return main[0][1]
            self.premierTour == 0
        carteAJoue = []
        carteTmp = 0
        color = 0
        self.analyseBonneCartes(main, 1)
        self.analyseMauvaiseCartes(main, 1)
        rangNb = 0
        valNb = 0
        rangLot = 0
        valLot = 0
        for i in range (0,4):
            if valNb < self.scoreNbCartesJoue[i]:
                valNb = self.scoreNbCartesJoue[i]
                rangNb = i
        if rangNb == 0:
            if self.scoreCartesJoue[4] <= 0:
                if self.scoreCartesJoue[5] <= 0:
                    if self.scoreCartesJoue[6] <= 0:
                        color = 'D'
                    elif self.scoreCartesJoue[7] <= 0:
                        color = 'S'
                elif self.scoreCartesJoue[6] <= 0:
                    if self.scoreCartesJoue[7] <= 0:
                        color = 'H'
            elif self.scoreCartesJoue[5] <= 0:
                if self.scoreCartesJoue[6] <= 0:
                    if self.scoreCartesJoue[7] <= 0:
                        color = 'C'
            if color != 0:
                for q in range(0,5):
                    if main[0][q]['color'] == color:
                        return main[0][q]
                    else:
                        return main[0][2]
            if self.scoreCartesJoue[0] > self.sommeCarteJoue[1]:
                for carte in main[0]:
                    if (carte['color'] == 'D') or (carte['color'] == 'H'):
                        carteTmp += carte
            elif self.scoreCartesJoue[0] < self.sommeCarteJoue[1]:
                for carte in main[0]:
                    if (carte['color'] == 'C') or (carte['color'] == 'S'):
                        carteTmp += carte
            for p in len(carteTmp):
                if main[0][p]['color'] == color:
                    return main[0][p]['color']
            return main[0][2]
        if rangNb == 1:
            for a in range(0,1):
                if valLot < self.scoreUnLotJoue[a]:
                    valLot = self.scoreUnLotJoue[a]
                    rangLot = a
            if rangLot == 0:
                if self.scoreCartesJoue[4] <= 0:
                    if self.scoreCartesJoue[5] <= 0:
                        if self.scoreCartesJoue[6] <= 0:
                            color = 'D'
                        elif self.scoreCartesJoue[7] <= 0:
                            color = 'S'
                    elif self.scoreCartesJoue[6] <= 0:
                        if self.scoreCartesJoue[7] <= 0:
                            color = 'H'
                elif self.scoreCartesJoue[5] <= 0:
                    if self.scoreCartesJoue[6] <= 0:
                        if self.scoreCartesJoue[7] <= 0:
                            color = 'C'
                if color != 0:
                    ind = 0
                    while len(carteAJoue) != 2:
                        if main[0][ind]['color'] == color:
                            carteAJoue += main[0][ind]
                    return carteAJoue
                else:
                    carteAJoue += main[0][0]
                    carteAJoue += main[0][1]
                    return  carteAJoue
                if self.scoreCartesJoue[0] > self.sommeCarteJoue[1]:
                    for carte in main[0]:
                        if (carte['color'] == 'D') or (carte['color'] == 'H'):
                            carteTmp += carte
                elif self.scoreCartesJoue[0] < self.sommeCarteJoue[1]:
                    for carte in main[0]:
                        if (carte['color'] == 'C') or (carte['color'] == 'S'):
                            carteTmp += carte
                for p in len(carteTmp):
                    max = len(carteTmp)
                    j = 0
                    while j < max:
                        if carteTmp[p]['number'] == carteTmp[j]['number']:
                            carteAJoue += carteTmp[p]
                            carteAJoue += carteTmp[j]
                        j += 1
                if len(carteAJoue) != 0:
                    return carteAJoue
                else:
                    carteAJoue = main[0][0]
                    carteAJoue += main[0][1]
                    return carteAJoue
            if rangLot == 1:
                if self.scoreCartesJoue[4] <= 0:
                    if self.scoreCartesJoue[5] <= 0:
                        if self.scoreCartesJoue[6] <= 0:
                            color = 'D'
                        elif self.scoreCartesJoue[7] <= 0:
                            color = 'S'
                    elif self.scoreCartesJoue[6] <= 0:
                        if self.scoreCartesJoue[7] <= 0:
                            color = 'H'
                elif self.scoreCartesJoue[5] <= 0:
                    if self.scoreCartesJoue[6] <= 0:
                        if self.scoreCartesJoue[7] <= 0:
                            color = 'C'
                if color != 0:
                    for y in range(0,4):
                        j = 0
                        while j < 4:
                            if main[0][y]['number'] == main[0][j]['number']:
                                if main[0][y]['color'] == color and main[0][j]['color'] == color:
                                    carteAJoue += main[0][y]
                                    carteAJoue += main[0][j]
                            j += 1
                    if len(carteAJoue) != 0:
                        return carteAJoue
                    else:
                        carteAJoue = main[0][0]
                        carteAJoue += main[0][1]
                        return carteAJoue
                if self.scoreCartesJoue[0] > self.sommeCarteJoue[1]:
                    for carte in main[0]:
                        if (carte['color'] == 'D') or (carte['color'] == 'H'):
                            carteTmp += carte
                elif self.scoreCartesJoue[0] < self.sommeCarteJoue[1]:
                    for carte in main[0]:
                        if (carte['color'] == 'C') or (carte['color'] == 'S'):
                            carteTmp += carte
                for t in len(carteTmp):
                    max = len(carteTmp)
                    j = 0
                    while j < max:
                        if carteTmp[t]['number'] == carteTmp[j]['number']:
                            carteAJoue += carteTmp[t]
                            carteAJoue += carteTmp[j]
                        j += 1
                if len(carteAJoue) != 0:
                    return carteAJoue
                else:
                    carteAJoue = main[0][0]
                    carteAJoue += main[0][1]
                    return carteAJoue
        if rangNb == 2:
            for a in range(0,2):
                if valLot < self.scoreUnLotJoue[a]:
                    valLot = self.scoreUnLotJoue[a]
                    rangLot = a
            if rangLot == 1 or rangLot == 0:
                if self.scoreUnLotMain[2] != 0:
                    for z in range(0, 3):
                        j = 0
                        while j < 4:
                            if main[0][z]['number'] == main[0][j]['number']:
                                carteAJoue += main[0][z]
                                carteAJoue += main[0][j]
                            j += 1
                    if len(carteAJoue) != 0:
                        return carteAJoue
                    else:
                        carteAJoue = main[0][0]
                        carteAJoue += main[0][1]
                        return carteAJoue
                else:
                    return ''
            if rangLot == 2:
                if self.scoreUnLotMain[2] != 0:
                    for r in range(0, 3):
                        j = 0
                        while j < 4:
                            if main[0][r]['number'] == main[0][j]['number']:
                                carteAJoue += main[0][r]
                                carteAJoue += main[0][j]
                            j += 1
                    if len(carteAJoue) == 3:
                        return carteAJoue
                    else:
                        carteAJoue = main[0][0]
                        carteAJoue += main[0][1]
                        carteAJoue += main[0][2]
                        return carteAJoue
                else:
                    return ''



    def calculScoreRougeNoir(self, carte, sens, tableau):
        scoreCartes = [0,0]
        if (carte['color'] == 'D') or (carte['color'] == 'H'):
            if sens == '+':
                scoreCartes[0] += 1
            elif sens == '-':
                scoreCartes[0] -= 1
        elif (carte['color'] == 'C') or (carte['color'] == 'S'):
            if sens == '+':
                scoreCartes[1] += 1
            elif sens == '-':
                scoreCartes[1] -= 1
        for i in range(0, len(scoreCartes)):
            if tableau == 0:
                self.scoreCartesJoue[i] += scoreCartes[i]
            elif tableau == 1:
                self.scoreCartesMain[i] += scoreCartes[i]



    def calculScoreParite(self, carte, sens, tableau):
        scoreCartes = [0,0,0,0]
        valeur = int(carte['number'])
        if (valeur % 2) == 0:
            if sens == '+':
                scoreCartes[2] += 1
            elif sens == '-':
                scoreCartes[2] -= 1
        elif (valeur % 2) == 1:
            if sens == '+':
                scoreCartes[3] += 1
            elif sens == '-':
                scoreCartes[3] -= 1
        for i in range(0, len(scoreCartes)):
            if tableau == 0:
                self.scoreCartesJoue[i] += scoreCartes[i]
            elif tableau == 1:
                self.scoreCartesMain[i] += scoreCartes[i]


    def calculScoreFigure(self, carte, sens, tableau):
        scoreCartes = [0,0,0,0,0,0,0,0]
        if carte['color'] == 'C':
            if sens == '+':
                scoreCartes[4] += 1
            elif sens == '-':
                scoreCartes[4] -= 1
        elif carte['color'] == 'H':
            if sens == '+':
                scoreCartes[5] += 1
            elif sens == '-':
                scoreCartes[5] -= 1
        elif carte['color'] == 'S':
            if sens == '+':
                scoreCartes[6] += 1
            elif sens == '-':
                scoreCartes[6] -= 1
        elif carte['color'] == 'D':
            if sens == '+':
                scoreCartes[7] += 1
            elif sens == '-':
                scoreCartes[7] -= 1
        for i in range(0, len(scoreCartes)):
            if tableau == 0:
                self.scoreCartesJoue[i] += scoreCartes[i]
            elif tableau == 1:
                self.scoreCartesMain[i] += scoreCartes[i]



    def calculScoreNumero(self, carte, sens, tableau):
        scoreCartes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if carte['number'] == 1:
            if sens == '+':
                scoreCartes[8] += 1
            elif sens == '-':
                scoreCartes[8] -= 1
        elif carte['number'] == 2:
            if sens == '+':
                scoreCartes[9] += 1
            elif sens == '-':
                scoreCartes[9] -= 1
        elif carte['number'] == 3:
            if sens == '+':
                scoreCartes[10] += 1
            elif sens == '-':
                scoreCartes[10] -= 1
        elif carte['number'] == 4:
            if sens == '+':
                scoreCartes[11] += 1
            elif sens == '-':
                scoreCartes[11] -= 1
        elif carte['number'] == 5:
            if sens == '+':
                scoreCartes[12] += 1
            elif sens == '-':
                scoreCartes[12] -= 1
        elif carte['number'] == 6:
            if sens == '+':
                scoreCartes[13] += 1
            elif sens == '-':
                scoreCartes[13] -= 1
        elif carte['number'] == 7:
            if sens == '+':
                scoreCartes[14] += 1
            elif sens == '-':
                scoreCartes[14] -= 1
        elif carte['number'] == 8:
            if sens == '+':
                scoreCartes[15] += 1
            elif sens == '-':
                scoreCartes[15] -= 1
        elif carte['number'] == 9:
            if sens == '+':
                scoreCartes[16] += 1
            elif sens == '-':
                scoreCartes[16] -= 1
        elif carte['number'] == 10:
            if sens == '+':
                scoreCartes[17] += 1
            elif sens == '-':
                scoreCartes[17] -= 1
        elif carte['number'] == 11:
            if sens == '+':
                scoreCartes[18] += 1
            elif sens == '-':
                scoreCartes[18] -= 1
        elif carte['number'] == 12:
            if sens == '+':
                scoreCartes[19] += 1
            elif sens == '-':
                scoreCartes[19] -= 1
        elif carte['number'] == 13:
            if sens == '+':
                scoreCartes[20] += 1
            elif sens == '-':
                scoreCartes[20] -= 1
        for i in range(0, len(scoreCartes)):
            if tableau == 0:
                self.scoreCartesJoue[i] += scoreCartes[i]
            elif tableau == 1:
                self.scoreCartesMain[i] += scoreCartes[i]




    def calculScoreNbCartes(self, lot, sens, tableau):
        scoreNbCartes = [0,0,0,0,0]
        nbCarte = len(lot)
        if nbCarte == 1:
            if sens == '+':
                scoreNbCartes[0] += 1
            elif sens == '-':
                scoreNbCartes[0] -= 1
        elif nbCarte == 2:
            if sens == '+':
                scoreNbCartes[1] += 1
            elif sens == '-':
                scoreNbCartes[1] -= 1
        elif nbCarte == 3:
            if sens == '+':
                scoreNbCartes[2] += 1
            elif sens == '-':
                scoreNbCartes[2] -= 1
        elif nbCarte == 4:
            if sens == '+':
                scoreNbCartes[3] += 1
            elif sens == '-':
                scoreNbCartes[3] -= 1
        elif nbCarte == 5:
            if sens == '+':
                scoreNbCartes[4] += 1
            elif sens == '-':
                scoreNbCartes[4] -= 1
        for i in range(0, len(scoreNbCartes)):
            if tableau == 0:
                self.scoreNbCartesJoue[i] += scoreNbCartes[i]
            elif tableau == 1:
                self.scoreNbCartesMain[i] += scoreNbCartes[i]


    def calculScoreUnLot(self, lot, sens, tableau):
        self.calculScoreCarteIdentique(lot, sens, tableau)
        self.calculScoreSuite(lot, sens, tableau)
        self.calculScoreCouleur(lot, sens, tableau)



    #Determine si un double, triple... doit etre joue
    def calculScoreCarteIdentique(self, lot, sens, tableau):
        scoreUnLot = [0,0,0,0]
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
                scoreUnLot[0] += 1
            elif sens == '-':
                scoreUnLot[0] -= 1
        elif compteur == 2:
            if sens == '+':
                scoreUnLot[1] += 1
            elif sens == '-':
                scoreUnLot[1] -= 1
        elif compteur == 3:
            if sens == '+':
                scoreUnLot[2] += 1
            elif sens == '-':
                scoreUnLot[2] -= 1
        elif compteur == 4:
            if sens == '+':
                scoreUnLot[3] += 1
            elif sens == '-':
                scoreUnLot[3] -= 1
        for i in range(0, len(scoreUnLot)):
            if tableau == 0:
                self.scoreUnLotJoue[i] += scoreUnLot[i]
            elif tableau == 1:
                self.scoreUnLotMain[i] += scoreUnLot[i]



    def calculScoreSuite(self, lot, sens, tableau):
        scoreUnLot = [0,0,0,0,0,0]
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
                scoreUnLot[4] += 1
            elif sens == '-':
                scoreUnLot[4] -= 1
        if suiteDecroissante == 1:
            if sens == '+':
                scoreUnLot[5] += 1
            elif sens == '-':
                scoreUnLot[5] -= 1
        for i in range(0, len(scoreUnLot)):
            if tableau == 0:
                self.scoreUnLotJoue[i] += scoreUnLot[i]
            elif tableau == 1:
                self.scoreUnLotMain[i] += scoreUnLot[i]



    def calculScoreCouleur(self, lot, sens, tableau):
        scoreUnLot = [0,0,0,0,0,0,0,0]
        couleurDifferente = 1
        memeCouleur = 1
        premiereCarte = 1
        ancienneCouleur = 1
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
                    scoreUnLot[6] += 1
                elif sens == '-':
                    scoreUnLot[6] -= 1
            if memeCouleur == 1:
                if sens == '+':
                    scoreUnLot[7] += 1
                elif sens == '-':
                    scoreUnLot[7] -= 1
        for i in range(0, len(scoreUnLot)):
            if tableau == 0:
                self.scoreUnLotJoue[i] += scoreUnLot[i]
            elif tableau == 1:
                self.scoreUnLotMain[i] += scoreUnLot[i]


    def calculScoreSommeNumero(self, lot, ancienLot, sens, tableau):
        sommeCarte = [0,0,0,0]
        total = 0
        totalAncien = 0
        for carte in lot:
            total += int(carte['number'])
        for carte in ancienLot:
            totalAncien += int(carte['number'])
        if total == totalAncien:
            if sommeCarte[0] == total:
                if sens == '+':
                    sommeCarte[1] += 1
                elif sens == '-':
                    sommeCarte[1] -= 1
            else:
                if sens == '+':
                    sommeCarte[1] = 1
                elif sens == '-':
                    sommeCarte[1] = -1
            sommeCarte[0] = total
        if sommeCarte[1] > sommeCarte[3]:
            sommeCarte[3] = sommeCarte[1]
            sommeCarte[2] = sommeCarte[0]
        for i in range(0, len(sommeCarte)):
            if tableau == 0:
                self.sommeCarteJoue[i] += sommeCarte[i]
            elif tableau == 1:
                self.sommeCarteMain[i] += sommeCarte[i]


if __name__ == '__main__':
    m = Joueur()
    m.jouerCartes('bidon')
