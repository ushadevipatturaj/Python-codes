import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s = 'X'
p2s = 'O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if count==3:
            return  True
    return  False
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if count==3:
            return True
    return False
def check_diagnals(symbol):
    if(board[0][0]==board[1][1] and board[1][1] == board[2][2] and board[2][2] == symbol):
        return True
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0]==symbol):
        return True
    else:
        return False
def win(symbol):
    if check_rows(symbol) or check_col(symbol) or check_diagnals(symbol):
        return True
    else:
        return False
def place(symbol):
    print(numpy.matrix(board))
    row=int(input("Enter Row Num 1 or 2 or 3 -"))
    col = int(input("Enter Col Num 1 or 2 or 3 -"))
    while (1):
        if(row > 0 and row <4 and col >0 and col <4 and board[row-1][col-1]=='-'):
            break
        else:
            print("Invalid Values ! Try Again")
    board[row-1][col-1]=symbol


def play():
    for i in range(9):
        if (i%2==0):
            print("X turn")
            place(p1s)
            if win(p1s):
                print(p1s,"Won")
                break

        else:
            print("O turn")
            place(p2s)
            if(win(p2s)):
                print(p2s,"won")
                break
        if (not win(p1s) and not win(p2s)):
            print("Draw")
play()