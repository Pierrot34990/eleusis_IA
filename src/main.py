#!/usr/bin/env python3
# -*- coding:Utf8 -*-

from webServiceFactory import WebServiceFactory
from joueur import Joueur
from god import God
import time, json

class Main:

    idJoueur = 0
    numJoueur = 0
    god = God()
    gameAlreadyStart = False
    CONST_DIEUX_INVENTE_UNE_REGLE = 0
    CONST_DIEUX_VERIFIE_DES_CARTES = 1
    CONST_DIEUX_DIT_SI_PROPHETE = 2

    def launch(self):
        endGame = False
        self.connect()

        while endGame == False:
            result = self.turn(self.idJoueur)
            if result['commencerPartie'] == True and self.gameAlreadyStart == False:
                self.numJoueur = self.ready(self.idJoueur)
                self.gameAlreadyStart = True
            else:
                if result['finPartie'] == True:
                    print("Fin de partie !!")
                else:
                    if result['status'] == 1:
                        print ("C'est à moi de jouer")
                        if self.numJoueur == 'god':
                            print ("Jouer en tant que Dieu .")
                            if result['godRole'] == self.CONST_DIEUX_INVENTE_UNE_REGLE:
                                rule = self.god.getRandomRule()
                                #self.sendRule(rule)
                                print ("Jouer en tant que Dieu, J'invente une règle...")
                                print(self.god.displayRule(rule))
                            elif result['godRole'] == self.CONST_DIEUX_DIT_SI_PROPHETE:
                                print("Jouer en tant que Dieu, Je dit prophète.")
                                if self.god.checkIfProphet() == True:
                                    print("True")
                                else:
                                    print("False")
                            elif result['godRole'] == self.CONST_DIEUX_VERIFIE_DES_CARTES:
                                print("Jouer en tant que Dieu, Je vérifie les cartes.")
                                if self.god.checkRules(result['partie']['selectedCards']) == False:
                                    return("False")
                                else:
                                    print("True")
                                #self.checkCards(self, result['partie']['selectedCards'])
                        else:
                            print ("Jouer en tant que joueur .")
                            self.playCards(result['partie'])
                    else:
                        print("C'est pas à moi de jouer !!")

            time.sleep(1)

    def connect(self):
        w = WebServiceFactory()
        self.idJoueur = w.webServiceConnect()

    def turn(self, idPlayer):
        w = WebServiceFactory()
        response = w.webServiceTurn(idPlayer)
        return response

    def ready(self, idPlayer):
        w = WebServiceFactory()
        response = w.webServiceReady(idPlayer)
        return response

    #def sendRule(self, rule):
    #    w = WebServiceFactory()
    #    response = w.webServiceSendRule(rule)
    #    return response

    def playCards(self, detailsPartie):
        IA = Joueur()
        cards = IA.jouerCartes(detailsPartie)
        w = WebServiceFactory()
        response = w.webServiceSendCards(cards)
        print(response)
        return response

    def getCardsTest(self):
        return json.dumps({'color': 'S','number': 2})

if __name__ == '__main__':
    m = Main()
    m.launch()