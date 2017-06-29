import time, json

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
    suiteAsc = 0
    suiteDesc = 0
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

    #sous-tableaux de score
    scoreNbCartes = [lotDe1,lotDe2,lotDe3,lotDe4, lotDe5]
    scoreUnLot = [simple, double, triple, quadruple, suiteAsc, suiteDesc, couleur1sur2, memeCouleur]
    scoreCartes = [rouge, noir, pair, impaire, trefles, coeur, piques, carreau, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize]
    #scoreSuiteLots = [carteSup, carteInf]

    #tableau final
    score = [scoreNbCartes, scoreUnLot, scoreCartes]

    def jouerCartes(self, detailsPartie):
        partie = json.loads(detailsPartie)
        self.analyseBonneCartes(partie['bonnes-cartes'])
        self.analyseMauvaiseCartes(partie['mauvaises-cartes'])
        cartes = self.choisirCartes()
        if cartes == None:
            return 'prophete'
        return cartes

    def analyseBonneCartes(self, lotsDeCartes):
        for lot in lotsDeCartes:
            self.calculScoreNbCarte(lot)

    def analyseMauvaiseCartes(self, lotsDeCartes):

    def choisirCartes(self):
        return

    def calculScoreNbCartes(self, lot):


