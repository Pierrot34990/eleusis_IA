import json

class Main:

    numCard = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    peer = ['yes','no']
    cardType = ['S', 'D', 'C', 'H']
    colorPlayed = []
    colorsChecked = 0
    numberCardsToPut = [1,2,3,4,5]
    redundancy = [0,1,2,3,4]  # The number of intermediate(s) card(s)
    alternancy = ['yes', 'no']  # ex : One red card then one black card

    def getCardsTest(self):
        data = json.dumps({'cards':[{'color': 'S','number': 2}, {'color':'C','number':3}]})
        return data

    def getFakeRule(self):
        data = {'numberCardsToPut':2,'color':'noir','numCard':None,'cardType':None,'redundancy':0, 'alternancy':'no'}
        return data

    # Check if rule is respected on cards played
    def checkRules(self):
        cardsPlayed = self.getCardsTest()
        item_dict = json.loads(cardsPlayed)
        rule = self.getFakeRule()
        ruleColor = rule['color']
        nbCardsToPut = rule['numberCardsToPut']
        print self.checkAllColors(item_dict,ruleColor)
        print self.checkNbCards(item_dict,nbCardsToPut)


    def checkAllColors(self,item_dict,ruleColor):
        for i in item_dict['cards']:
            if (i['color'] == 'D') or (i['color'] == 'H'):
                self.colorPlayed.append('rouge')
            elif(i['color'] == 'C') or (i['color'] == 'S'):
                self.colorPlayed.append('noir')
                for j in self.colorPlayed:
                    if j == ruleColor:
                        self.colorsChecked += 1
        if len(self.colorPlayed) == len(item_dict['cards']):
            return "Bonne couleurs"
        else:
            return "Mauvaises couleurs"

    def checkNbCards(self,item_dict,nbCardsToPut):
        if len(item_dict['cards']) == nbCardsToPut:
            return "Bon nb de cartes"
        else:
            return "Mauvais nombre de cartes"

if __name__ == '__main__':
    m = Main()
    m.checkRules()