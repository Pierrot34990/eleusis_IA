#!/usr/bin/env python3
# -*- coding:Utf8 -*-

import requests, json

class WebServiceFactory:

    def __init__(self):
        self.URL_CONNECT = "http://127.0.0.1:8000/app_dev.php/"
        self.URL_RULE = "http://127.0.0.1:8000/app_dev.php/god-choose-rules/"

    def webServiceConnect(self):
        response = requests.get(self.URL_CONNECT + 'connect/nao')
        json_data = json.loads(response.text)

        return json_data['idJoueur']

    def webServiceTurn(self, idJoueur):
        response = requests.get(self.URL_CONNECT + 'turn/' + str(idJoueur))
        json_data = json.loads(response.text)

        return json_data

    def webServiceReady(self, idJoueur):
        response = requests.get(self.URL_CONNECT + 'ready/' + str(idJoueur))
        json_data = json.loads(response.text)

        return json_data['numJoueur']

    def webServiceSendRule(self, rule):

        response = requests.post(self.URL_RULE + json.dumps(rule))
        print("URL  = " + str(self.URL_RULE + json.dumps(rule)))
        return response