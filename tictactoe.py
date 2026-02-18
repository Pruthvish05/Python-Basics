def box():
    for i in range(3):
        print("****"*4)
        for j in range(3):
            print("|    "*4)
#box()
def tic_tac_toe():
    i=int(input("Enter row number (0-2): "))
    j=int(input("Enter column number (0-2): "))
    if i<0 or i>2 or j<0 or j>2:
        print("Invalid input. Please enter numbers between 0 and 2.")
    else:
        while True:
                for x in range(3):
                    for y in range(3):
                        if x==i and y==j:
                            print("X ", end="")
                        else:
                            print("- ", end="")
                        print()

def tic_tac_toe1():
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    lst=[]
    i1=int(input("Enter row number of player 1 (0-2): "))
    j1=int(input("Enter column number of player 1 (0-2): "))
    i2=int(input("Enter row number of player 2 (0-2): "))
    j2=int(input("Enter column number of player 2 (0-2): "))
    if i1<0 or i1>2 or j1<0 or j1>2:
        print("Invalid input for player 1. Please enter numbers between 0 and 2.")
    elif i2<0 or i2>2 or j2<0 or j2>2:
        print("Invalid input for player 2. Please enter numbers between 0 and 2.")
    elif i1==i2 and j1==j2:
        print("Both players cannot choose the same position. Please try again.")
    else:
        board[i1][j1]='X'
        board[i2][j2]='O'
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    lst.append((i1,j1))
    lst.append((i2,j2))
tic_tac_toe1()

