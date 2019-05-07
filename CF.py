def column(current_choose):
    if int(current_choose)<=3:
        return 0
    elif int(current_choose)>3 and int(current_choose)<=6:
        return 1
    elif int(current_choose)>6 and int(current_choose)<=9:
        return 2

def same_columns(table):
    i=0
    for x in range(3):
        if table[i][x]==table[i+1][x]==table[i+2][x]:
            return True
        else:
            return False
