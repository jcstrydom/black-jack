# ## These are GLOBALLY used variables
# # The below is the dictionary for the forms
# valDict = {' A':cf.ac,' 2':cf.tw,' 3':cf.th,' 4':cf.fo,' 5':cf.fi,' 6':cf.si,' 7':cf.se,' 8':cf.ei,' 9':cf.ni,'10':cf.te,' J':cf.ja,' Q':cf.qu,' K':cf.ki}
# # The below is the dictionary for the suitToken to be used
# suitDict = {'Di':cf.diT,'Cl':cf.clT,'Hr':cf.hrT,'Sp':cf.spT}
# # The below is the dictionary for the suit form to be used
# suitFormDict = {'Di':cf.diamonds,'Cl':cf.clubs,'Hr':cf.hearts,'Sp':cf.spades}


# class Values:

#       def __init__(self):
#             pass


diamonds = ('   00    ',
            '  0000   ',
            ' 000000  ',
            '00000000 ',
            ' 000000  ',
            '  0000   ',
            '   00    ',
            '         ',
            '         ')

hearts = (' 00   00 ',
          '0000 0000',
          '000000000',
          '000000000',
          ' 0000000 ',
          '  00000  ',
          '   000   ',
          '    0    ',
          '         ',)

clubs = ('   000   ',
         '  00000  ',
         '   000   ',
         ' 0  0  0 ',
         '000 0 000',
         '000000000',
         ' 0  0  0 ',
         '   000   ',
         '         ')


spades = ('    0    ',
          '   000   ',
          ' 0000000 ',
          '000000000',
          '000000000',
          ' 00   00 ',
          '    0    ',
          '   000   ',
          '         ')

ja = ('         ',
      '         ',
      '         ',
      '         ',
      '        0',
      '        0',
      '        0',
      '    0   0',
      '     000 ')

qu = ('         ',
      '         ',
      '         ',
      '         ',
      '    0000 ',
      '   0    0',
      '   0  0 0',
      '   0   00',
      '    000 0')

ki = ('         ',
      '         ',
      '         ',
      '         ',
      '    0   0',
      '    0  0 ',
      '    000  ',
      '    0  0 ',
      '    0   0')


tw = ('         ',
      '         ',
      '         ',
      '         ',
      '     00  ',
      '    0  0 ',
      '      0  ',
      '     0   ',
      '    0000 ')

th = ('         ',
      '         ',
      '         ',
      '         ',
      '    000  ',
      '   0   0 ',
      '      0  ',
      '   0   0 ',
      '    000  ')

fo = ('         ',
      '         ',
      '         ',
      '         ',
      '       0 ',
      '      00 ',
      '     0 0 ',
      '    0000 ',
      '       0 ')

fi = ('         ',
      '         ',
      '         ',
      '         ',
      '    0000 ',
      '    0    ',
      '    000  ',
      '       0 ',
      '    0000 ')


si = ('         ',
      '         ',
      '         ',
      '         ',
      '    000   ',
      '   0     ',
      '   0000  ',
      '   0   0 ',
      '    000  ')

se = ('         ',
      '         ',
      '         ',
      '         ',
      '    0000 ',
      '       0 ',
      '      0  ',
      '     0   ',
      '     0   ')

ei = ('         ',
      '         ',
      '         ',
      '         ',
      '     00  ',
      '    0  0 ',
      '     00  ',
      '    0  0 ',
      '     00  ')

ni = ('         ',
      '         ',
      '         ',
      '         ',
      '    000  ',
      '   0   0 ',
      '    0000 ',
      '       0 ',
      '    000  ')


te = ('         ',
      '         ',
      '         ',
      '         ',
      '  0  000 ',
      '  0 0   0',
      '  0 0   0',
      '  0 0   0',
      '  0  000 ')

ac = ('         ',
      '         ',
      '         ',
      '         ',
      '     0   ',
      '    0 0  ',
      '   0   0 ',
      '   00000 ',
      '   0   0 ')


spT = '\u2660'
clT = '\u2663'
hrT = '\u2665'
diT = '\u2666'

tlC = '\u2554'
trC = '\u2557'
blC = '\u255A'
brC = '\u255D'
hrL = '\u2550'
vrL = '\u2551'
blK = '\u2592'


if __name__=="__main__":
      print('This seems to work')
