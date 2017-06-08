#!/usr/bin/env python3
# -*- coding:Utf8 -*-

from webServiceFactory import WebServiceFactory
import time

class Main:

    idJoueur = 0

    def launch(self):

        endGame = False
        self.connect()

        while endGame == False:
            result = self.turn(self.idJoueur)

            if result['commencerPartie'] == True:
                print('C\'est à moi de jouer !!')
            else:
                print('C\'est pas à moi de jouer !!')

            time.sleep(1)

    def connect(self):

        w = WebServiceFactory()
        self.idJoueur = w.webServiceConnect()

    def turn(self, idPlayer):

        w = WebServiceFactory()
        response = w.webServiceTurn(idPlayer)
        return response

if __name__ == '__main__':
    m = Main()
    m.launch()