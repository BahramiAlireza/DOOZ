from itertools import cycle
def play():
    tabel='''
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
'''
    while not is_matched():
        for player in cycle(['x','0']):
            inpt=input("{} position?".format(player))
            tabel=tabel.replace(inpt,player)
            print(tabel)
def draw_tabel():pass

def is_matched():
    return False

def place_choose(table):pass

