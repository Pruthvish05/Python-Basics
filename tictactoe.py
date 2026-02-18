def box():
    for i in range(3):
        print("****"*4)
        for j in range(3):
            print("|    "*4)
box()
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
tic_tac_toe()

