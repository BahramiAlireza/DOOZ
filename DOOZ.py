from itertools import cycle
from CF import column,same_columns

match_table=[[1,2,3],
             [4,5,6],
             [7,8,9]]

def play():
    table='''
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
'''
    while not is_matched():
        for player in cycle(['x','0']):
            inpt=input("{} position?".format(player))
            table=table.replace(inpt,player)
            redraw(player,int(inpt))
            if is_matched():
                print("player {} won!".format(player))
            else:
                print(table)

def is_matched():
    if match_table[0][0]==match_table[1][1]==match_table[2][2]:
        return True
    elif len(set(match_table[0]))==1 or len(set(match_table[1]))==1 or len(set(match_table[2]))==1:
        return True
    elif match_table[0][2]==match_table[1][1]==match_table[2][0]:
        return True
    elif same_columns(match_table):
        return True
    else:
        return False

def redraw(player,current_choose):
    for index,num in enumerate(match_table[column(current_choose)]):
        if num==current_choose:
            match_table[column(current_choose)][index]=player
