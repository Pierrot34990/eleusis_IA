#!/usr/bin/env python3
# -*- coding:Utf8 -*-

import requests, json

class WebServiceFactory:

    def __init__(self):
        self.URL_CONNECT = "http://localhost:8888/eleusis_IA/web/app_dev.php/"

    def webServiceConnect(self):
        response = requests.get(self.URL_CONNECT + 'connect/pierre')
        json_data = json.loads(response.text)

        return json_data['idJoueur']

    def webServiceTurn(self, idJoueur):
        response = requests.get(self.URL_CONNECT + 'turn/' + str(idJoueur))
        json_data = json.loads(response.text)

        return json_data
