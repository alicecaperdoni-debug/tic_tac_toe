from prettytable import PrettyTable
import art

t = PrettyTable()

### La tabella iniziale
t.field_names = ["¡", "1", "2", "3", "!"]
t.add_row(["1", "", "", "", "1"])
t.add_divider()
t.add_row(["2", "", "", "", "2"])
t.add_divider()
t.add_row(["3", "", "", "", "3"])
t.add_divider()
t.add_row(["", "1", "2", "3", ""])

##TODO Se riesci, migliora l'inserimento della coordinata
### Inserimento della "X"
def enter(player):
    enter_again = True
    while enter_again:
        row = int(input(f"{player} player, write the number of the row:"))
        column = int(input(f"{player} player, write the number of the column:"))
        global t
        if t.rows[row - 1][column] == "":
            t.rows[row - 1][column] = f"{player}"
            enter_again = False
        else:
            print("\nSomeone already played in this cell, please try other coordinates.\n")

#TODO AGGIUSTA CHECK WINNER!!!!!
def check_winner():
    global t
    global end_game

    if t.rows[1][1] == t.rows[1][2] == t.rows[1][3] or t.rows[2][1] == t.rows[2][2] == t.rows[2][3] or t.rows[3][1] == t.rows[3][2] == t.rows[3][3] or t.rows[1][1] == t.rows[2][1] == t.rows[3][1] or t.rows[1][2] == t.rows[2][2] == t.rows[3][2] or t.rows[1][3] == t.rows[2][3] == t.rows[3][3] or t.rows[1][1] == t.rows [2][2] == t.rows[3][3] or t.rows[1][3] == t.rows[2][2] == t.rows[3][1]:
            return True
    else:
        return False

print(art.logo)
print("Welcome to Alice's Tic Tac Toe game!")

end_game = False
turn = 0

while end_game == False:
    turn += 1
    print(turn)
    print(f"\n{t}\n")
    enter("X")
    print(f"\n{t}\n")

    if turn >= 3:
        if check_winner():
            end_game = True
    if turn == 5:
        end_game = True

    enter("O")
    print(f"\n{t}\n")

    if turn >= 3:
        end_game = check_winner()
print(t.get_string())
# if check_winner():
#     if "X" in t.rows >= "O" in t.rows:
#         print("\"X\" wins!")
#TODO Scrivi la fine della partita, se c'è un vincitore o se è un pareggio


#TODO Nuova partita? Se sì resetta la tabella

###TODO Extra: possibilità di scegliere un giocatore (user vs. computer)
