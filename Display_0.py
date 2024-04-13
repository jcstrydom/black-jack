import math
import os

diamonds = ('    0    ',
            '   000   ',
            '  00000  ',
            ' 0000000 ',
            '000000000',
            ' 0000000 ',
            '  00000  ',
            '   000   ',
            '    0    ')

hearts = (' 000 000 ',
          '000000000',
          '000000000',
          ' 0000000 ',
          '  00000  ',
          '   000   ',
          '    0    ',
          '         ') 

clubs = ('   000   ',
         '  00000  ',
         '   000   ',
         ' 0  0  0 ',
         '000 0 000',
         '000000000',
         ' 00 0 00 ',
         '    0    ',
         '   000   ')


spades = ('    0    ',
          '   000   ',
          ' 0000000 ',
          '000000000',
          '000000000',
          '  00 00  ',
          '    0    ',
          '   000   ',
          '         ')

ja = ('       00',
      '       00',
      '       00',
      '       00',
      '       00',
      '00     00',
      '00     00',
      ' 00   00 ',
      '   000   ')

qu = ('   000   ',
      ' 00   00 ',
      '00     00',
      '00     00',
      '00     00',
      '00     00',
      '00  00 00',
      ' 00  000 ',
      '   000 00')

ki = ('00     00',
      '00     00',
      '00    00 ',
      '00  00   ',
      '0000     ',
      '0000     ',
      '00  00   ',
      '00    00 ',
      '00     00')

on = ('       00',
      '     0000',
      '  0000 00',
      '000    00',
      '       00',
      '       00',
      '       00',
      '       00',
      '       00')

tw = ('   000   ',
      ' 00   00 ',
      '00     00',
      '       00',
      '      00 ',
      '     00  ',
      '  000    ',
      '000      ',
      '000000000')

th = ('   000   ',
      ' 00   00 ',
      '00     00',
      '      00 ',
      '    000  ',
      '      00 ',
      '       00',
      '00    00 ',
      ' 000000  ')

fo = ('       00',
      '     0000',
      '   000 00',
      ' 000   00',
      '000    00',
      '000000000',
      '       00',
      '       00',
      '       00')

fi = (' 00000000',
      '000      ',
      '00       ',
      '0000000  ',
      '00    00 ',
      '       00',
      '       00',
      '00    00 ',
      ' 000000  ')


si = ('    0000 ',
      '  00   00',
      ' 00      ',
      '00  000  ',
      '000   00 ',
      '00     00',
      '00     00',
      ' 00   00 ',
      '   0000  ')

se = ('000000000',
      ' 00000000',
      '      000',
      '    000  ',
      '   00    ',
      '   00    ',
      '   00    ',
      '   00    ',
      '   00    ',
      '   00    ')

ei = ('   000   ',
      ' 00   00 ',
      '00     00',
      ' 00   00 ',
      '  00000  ',
      ' 00   00 ',
      '00     00',
      '00     00',
      ' 0000000 ')

ni = ('  0000   ',
      '000   00 ',
      '00     00',
      '00     00',
      ' 00   000',
      '   000 00',
      '       00',
      ' 00   00 ',
      '  00000  ')


te = ('00   00  ',
      '00  0  0 ',
      '00 0    0',
      '00 0    0',
      '00 0    0',
      '00 0    0',
      '00 0    0',
      '00  0  0 ',
      '00   00  ')

ac = ('  000    ',
      ' 00000   ',
      '00   00  ',
      '00    00 ',
      '00     00',
      '000000000',
      '00     00',
      '00     00',
      '00     00')


spT = '\u2660'
clT = '\u2663'
hrT = '\u2665'
diT = '\u2666'


#print('u2660: '+spT)
#print('u2663: '+clT)
#print('u2665: '+hrT)
#print('u2664: '+diT)

valDict = {' A':ac,' 2':tw,' 3':th,' 4':fo,' 5':fi,' 6':si,' 7':se,' 8':ei,' 9':ni,'10':te,' J':ja,' Q':qu,' K':ki}
suitDict = {'Di':diT,'Cl':clT,'Hr':hrT,'Sp':spT}
suitFormDict = {'Di':diamonds,'Cl':clubs,'Hr':hearts,'Sp':spades}

os.system('cls')

def printValue(valTx,suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the value diagram as a string
    """
    vT = valDict(valTx)
    sT = suitDict(suitT)
    valueText = ''
    indx = math.floor(lineNum/2)
    for j in range(0,9):
        valueText += (vT[indx][j]*2)
    return valueText.replace('0',sT)



def printSuit(suitT,lineNum):
    """
    DOCSTRING: this brings back a specific line of the suit diagram as a string
    """
    if (lineNum < 9):
        sT = suitFormDict(suitT)
        suitText = ''
        for j in range(0,9):
            suitText += (sT[lineNum][j])
        return suitText.replace('0',sT)
    else:
        pass

