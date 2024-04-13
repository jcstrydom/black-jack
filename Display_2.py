import math
import os
import cardforms as cf
import time
from PIL import ImageFont as i_f



#print('u2660: '+spT)
#print('u2663: '+clT)
#print('u2665: '+hrT)
#print('u2664: '+diT)

valDict = {' A':cf.ac,' 2':cf.tw,' 3':cf.th,' 4':cf.fo,' 5':cf.fi,' 6':cf.si,' 7':cf.se,' 8':cf.ei,' 9':cf.ni,'10':cf.te,' J':cf.ja,' Q':cf.qu,' K':cf.ki}
suitDict = {'Di':cf.diT,'Cl':cf.clT,'Hr':cf.hrT,'Sp':cf.spT}
suitFormDict = {'Di':cf.diamonds,'Cl':cf.clubs,'Hr':cf.hearts,'Sp':cf.spades}
font = i_f.truetype('times.ttf',12)

# os.system('cls')

def printValue(valTx,suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the value diagram as a string
    """
    vT = valDict[valTx]
    sT = suitDict[suitT]
    valueTxt = ''
    indx = math.floor(lineNum/2)
    for j in range(0,9):    # here each line item is iterated through and doubled
        valueTxt += (vT[indx][j]*2)
    return valueTxt.replace('0',sT)



def printSuit(suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the suit diagram as a string
    """
    if (lineNum < 9):
        sT = suitDict[suitT]
        sF = suitFormDict[suitT]
        suitTxt = ''
        for x in range(0,9):
            suitTxt += sF[lineNum][x]
        return suitTxt.replace('0',sT)
    else:
        pass

def lineCombine(crds,lineNumber):
    finalLineText = cf.vrL
    for a in crds:
        valueText = a[2::]
        suitText = a[0:2]
        pV = (valueText,suitText,lineNumber)
        pS = (suitText,lineNumber)
        if lineNumber < 9:
            for k in range(0,len(pS)):
                if (pS[k] == pV[k]) and (pV[k-1] != ' '):
                    finalLineText += ' '
                else:
                    finalLineText += pS[k]
            finalLineText += (pV[len(pS)::]+ cf.vrL)
        else:
            finalLineText += (pV + cf.vrL)
    return finalLineText





num = 'J'
pack = ['Hr '+str(num),'Di '+str(num),'Cl '+str(num)]#,'Sp '+str(num),'Hr '+str(num),'Hr '+str(4),'Hr '+str(9)]
# print(pack)
# print(math.floor(len(pack)/4))
for levelCount in range(0,math.floor(len(pack)/4)+1):
    packStart = levelCount*4
    packEnd = min ((levelCount+1)*4,len(pack))
    # print(packStart)
    # print(packEnd)
    levelPack = pack[packStart:packEnd]
    # print(levelPack)
    cardNames = ''
    print('{:^200}'.format((cf.tlC + (cf.hrL) * 20  + cf.trC)*len(levelPack)))
    for lines in range(0,18):
        lineToPrint = lineCombine(levelPack,lines)
        # size_vt,x = font.getsize(lineToPrint)
        # size_sp,x = font.getsize('\u2008')
        # vt_multiplyer = math.floor((216 - size_vt) / size_sp)
        # lineToPrint += '\u2008'*vt_multiplyer
        print('{:^200}'.format(lineToPrint))

    for b in levelPack:
        valueText = b[2::]
        suitText = b[0:2]
        cardNames += suitText + ' ' + valueText + ' '*18
    print('{:^200}'.format((cf.blC + (cf.hrL) * 20 + cf.brC)*len(levelPack)))
    print('{:^200}'.format(cardNames))


# How to get the pixel size to get the spacing correct
# https://stackoverflow.com/questions/35771863/how-to-calculate-length-of-string-in-pixels-for-specific-font-and-size













