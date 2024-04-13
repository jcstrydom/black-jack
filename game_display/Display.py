import math
import os
import cardforms as cf
import time


## These are GLOBALLY used variables
# The below is the dictionary for the forms
# valDict = {' A':cf.ac,' 2':cf.tw,' 3':cf.th,' 4':cf.fo,' 5':cf.fi,' 6':cf.si,' 7':cf.se,' 8':cf.ei,' 9':cf.ni,'10':cf.te,' J':cf.ja,' Q':cf.qu,' K':cf.ki}
valDict = {'A':cf.ac,'2':cf.tw,'3':cf.th,'4':cf.fo,'5':cf.fi,'6':cf.si,'7':cf.se,'8':cf.ei,'9':cf.ni,'10':cf.te,'J':cf.ja,'Q':cf.qu,'K':cf.ki}
# The below is the dictionary for the suitToken to be used
suitDict = {'Di':cf.diT,'Cl':cf.clT,'Hr':cf.hrT,'Sp':cf.spT}

# The below is the dictionary for the suit form to be used
suitFormDict = {'Di':cf.diamonds,'Cl':cf.clubs,'Hr':cf.hearts,'Sp':cf.spades}


### NOT Gonna use this at the moment
class CardForms:

    def __init__(self):
        values = ['a','2','3','3','4','5','6','7','8','9','10','j','q','k']
        value_forms = [cf.ac, cf.tw, cf.th, cf.fo, cf.fi, cf.si, cf.se, cf.ei, cf.ni, cf.te, cf.ja, cf.qu, cf.ki]
        suites = ['Di', 'Cl', 'Hr', 'Sp']
        suite_tokens = [cf.diT, cf.clT, cf.hrT, cf.spT]
        suite_forms = [cf.diamonds, cf.clubs, cf.hearts,cf.spades]
        
        self.values = [f'{e.upper()}' for e in values]
        self.value_forms = {l:t for l,t in zip(self.vaules,value_forms)}
        self.suites = suites
        self.suite_tokens = {l:t for l,t in zip(self.suites,suite_tokens)}
        self.suite_forms = {l:t for l,t in zip(self.suites,suite_forms)}



class __Player():
    '''
    DOCSTRING: this class is only to instantiate a player for the testing area (where __name__ == "__main__")
    '''
    is_pc = False


    def __init__(self,name,balance=100):
        '''
        DOCSTRING: this instantiates a player object with the player name
        '''
        self.name = name
        self.bust = False
        self.score = 0
        self.balance = balance
        self.cards = []
        self.bet = 0


    def addCard(self,card):
        '''
        DOCSTRING: this adds a card
        '''
        self.cards.append(card)


    def getCard(self):
        '''
        DOCSTRING: this returns the cards
        '''
        return self.cards

    def getName(self):
        '''
        DOCSTRING: this returns the name of the player
        '''
        return self.name

    def __str__(self):
        """
        DOCSTRING: this returns the players name only
        """
        return self.name


def printValue(valTx,suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the value diagram as a string
    """
    vT = valDict[valTx]             # this gives the form to be implemented
    sT = suitDict[suitT]            # this gives the suit token
    valueTxt = ''
    indx = math.floor(lineNum/2)
    for j in range(0,9):            # here each line item is iterated through AND DOUBLED
        valueTxt += (vT[indx][j]*2)
    # print('ValueText type: ' + str(type(suitText)))
    return valueTxt.replace('0',sT)



def printSuit(suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the suit diagram as a string
    """
    if (lineNum < 9):
        sT = suitDict[suitT]        # This gives the token to be used
        sF = suitFormDict[suitT]    # This gives the form to be implemented
        suitTxt = ''
        for x in range(0, 9):
            suitTxt += sF[lineNum][x]
        return suitTxt.replace('0', sT)
    else:
        pass



def lineCombine(cards,lineNumber,plrName='PC1',lvlCount=0,isFinalRound=False):
    """
    DOCSTRING: this is the combining of the suit and the value forms for all the cards
    NOTE: this combination happens one line at a time
    """
    finalLineText = ''
    for i,a in enumerate(cards):                  
        finalLineText += cf.vrL
        if plrName == 'House' and (i == 0) and lvlCount ==0 and not isFinalRound:
            pV = cf.blK*18
            pS = cf.blK*9
        else:
            # valueText = a[2::]
            # suitText = a[0:2]
            suitText, valueText = [x for x in a.split(" ")]
            pV = printValue(valueText,suitText,lineNumber)
            pS = printSuit(suitText,lineNumber)
            # print(pS)
            # print(pV)
            # print('printValue type: ' +str(type(pV))+'; printSuit type: '+str(type(pS)))
        if lineNumber < 9:
            if plrName == 'House' and (i == 0) and lvlCount == 0 and not isFinalRound:
                finalLineText += pS + cf.blK*9 + cf.vrL
            else:
                finalLineText += pS + ' '*9 + cf.vrL
        else:
            finalLineText += pV + cf.vrL
    return finalLineText




def displayCards(pack,finalRound,playrName):
    """
    DOCSTRING: this function displays the cards that the player has
    NOTE: it also takes into account if the player is the house and blanks that first card
    """
    for levelCount in range(0,math.floor(len(pack)/6)+1):
        packStart = levelCount*6
        packEnd = min ((levelCount+1)*6,len(pack))
        levelPack = pack[packStart:packEnd]
        cardNames = ''

        ## This part writes the top of the card
        print('{:^200}'.format((cf.tlC + (cf.hrL) * 18  + cf.trC)*len(levelPack)))
        for lines in range(0,18):
            if lines == 8:
                pass
            else:
                lineToPrint = lineCombine(levelPack,lines,playrName,levelCount,finalRound)
                print('{:^200}'.format(lineToPrint))

        for b in levelPack:
            valueText = b[2::]
            suitText = b[0:2]
            if playrName == 'House' and (b == levelPack[0]) and levelCount ==0 and finalRound != True:
                cardNames += ' '*20
            else:
                cardNames += suitText + ' ' + valueText + ' '*15
        print('{:^200}'.format((cf.blC + (cf.hrL) * 18 + cf.brC)*len(levelPack)))
        print('{:^200}'.format(cardNames))



def display(player,isFinalRound=False):
    player_name = player.name
    pack = player.cards
    if player_name == "House":
        print('\t\t'+player_name+"'s cards:")
        displayCards(pack,isFinalRound,player_name)
    elif not player.bust:
        print('\t\t'+player_name+" has a score of "+str(player.score)+" with the following cards:")
        displayCards(pack,isFinalRound,player_name)
    elif player.bust:
        displayCards(pack,isFinalRound,player_name)
        print('\n' + '\t' * 10 + f'{player_name} has gone bust with a score of {player.score}!!!')

    

if __name__ == '__main__':
    pack = ['Hr J','Di K','Cl A','Sp 8','Hr 3','Hr 4','Hr 9','Cl 10']
    isFinalRound = True
    Pl1 = __Player("House")
    Pl1.cards = pack
    display(Pl1,isFinalRound)

