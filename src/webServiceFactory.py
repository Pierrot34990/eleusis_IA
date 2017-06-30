#!/usr/bin/env python3
# -*- coding:Utf8 -*-

import requests, json

class WebServiceFactory:

    def __init__(self):
        self.URL_CONNECT = "http://127.0.0.1:8000/"

    def webServiceConnect(self):
        response = requests.get(self.URL_CONNECT + 'connect/pierre')
        json_data = json.loads(response.text)

        return json_data['idJoueur']

    def webServiceTurn(self, idJoueur):
        response = requests.get(self.URL_CONNECT + 'turn/' + str(idJoueur))
        json_data = json.loads(response.text)

        return json_data
