from __future__ import print_function

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False
def printBoard() :
    print( '\n ')
    print( '\t' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] )
    print( '\t---------')
    print(  '\t' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] )
    print( '\t---------')
    print( '\t' +  choices[6] + ' | ' + choices[7] + ' | ' + choices[8])
    print( '\n')


while not winner :
    printBoard()

    if playerOneTurn :
        print( "\t Its turn of Player 1")
    else :
        print( "\t Its turn of Player 2")

    try:
        choice = int(input("Enter the Position you want to mark -> "))
    except:
        print("Oh! Please enter a valid field")
        continue
    if choices[choice - 1] == '#' or choices [choice-1] == 'O':
        print("Ooops! Illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = '#'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Congratulations!\n Player " + str(int(playerOneTurn + 1)) + " won!\n")
