""""
Algorithminn er:

 * Fá óskandi átt
 * Skoða hvort áttin sé lögleg með isValidMove()
 * Ef átt er lögleg þá framkvæmum við move()
 * Annars látum við notanda vita að átt er ólögleg
 * Skoðum x og y í hverri keyrslu og ef x = 3 og y = 1 þá prentum við Victorious og ljúkum keyrslu.
 
 https://github.com/PeturSteinn/Assignment-8-TileTraveller 


"""""

# direction = N/E/S/W

NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"


run = True
x = 1
y = 1


def isValidMove(x, y, direction):

    direction = direction.lower()

    if y == 1: # Bottom line in the grid
        if direction == NORTH:
            return True

    elif x == 1 and y == 2:
        if direction == NORTH or direction == SOUTH or direction == EAST:
            return True

    elif x == 2 and y == 2:
        if direction == SOUTH or direction or WEST:
            return True

    elif x == 3 and y == 2:
        if direction == NORTH or direction or SOUTH:
            return True
    
    elif x == 1 and y == 3:
        if direction == EAST or direction == SOUTH:
            return True

    elif x == 2 and y == 3:
        if direction == EAST or direction == WEST:
            return True
    elif x == 3 and y == 3:
        if direction == SOUTH or direction == WEST:
            return True

    return False


def getValidMoves(x,y): # (x,y)

    moves = ""

    if y == 1: # Bottom line in the grid
        moves = "(N)orth."

    elif x == 1 and y == 2:
        moves = "(N)orth or (E)ast or (S)outh."

    elif x == 2 and y == 2:
        moves = "(S)outh or (W)est."

    elif x == 3 and y == 2:
        moves = "(N)orth or (S)outh."
    
    elif x == 1 and y == 3:
        moves = "(E)ast or (S)outh."

    elif x == 2 and y == 3:
        moves = "(E)ast or (W)est."
    
    elif x == 3 and y == 3:
        moves = "(S)outh or (W)est."

    print(f"You can travel: {moves}")
    

def move(x, y, direction):
    direction = direction.lower()
    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == WEST:
        x -= 1
    elif direction == EAST:
        x += 1
    return x, y


def isVictorious(x,y): # (x,y)
    if x == 3 and y == 1:
        return True
    return False


while run:

    getValidMoves(x, y)
    direction = input("Direction: ")
    if isValidMove(x, y, direction):
        # Færum x og y ef þetta tekst
        print(isValidMove(x,y,direction))
        x, y = move(x, y, direction)

    else:
        print("Not a valid direction!")

    if isVictorious(x, y):
        print("Victory!")
        run = False