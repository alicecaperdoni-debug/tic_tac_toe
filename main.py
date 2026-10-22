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


### Inserimento della "X" o "O"
def enter(player):
    enter_again = True
    while enter_again:
        global t
        try:
            row = int(input(f"{player} player, write the number of the row:"))
        except ValueError or UnboundLocalError:
            print("You can only enter 1, 2 or 3.")
            continue
        try:
            column = int(input(f"{player} player, write the number of the column:"))
        except ValueError or UnboundLocalError:
            print("You can only enter 1, 2 or 3.")
            continue
        try:
            if t.rows[row - 1][column] == "":
                t.rows[row - 1][column] = f"{player}"
                enter_again = False
            else:
                print("\nSomeone already played in this cell, please try other coordinates.\n")
        except IndexError:
            print("You can only enter 1, 2 or 3.")


def check_winner():
    global t
    if (t.rows[0][1] == t.rows[0][2] == t.rows[0][3] != "") or (t.rows[1][1] == t.rows[1][2] == t.rows[1][3] != "") or (t.rows[2][1] == t.rows[2][2] == t.rows[2][3] != "") or (t.rows[0][1] == t.rows[1][1] == t.rows[2][1] != "") or (t.rows[0][2] == t.rows[1][2] == t.rows[2][2] != "") or (t.rows[0][3] == t.rows[1][3] == t.rows[2][3] != "") or (t.rows[0][1] == t.rows [1][2] == t.rows[2][3] != "") or (t.rows[0][3] == t.rows[1][2] == t.rows[2][1] != ""):
            return True
    else:
        return False

print(art.logo)
print("Welcome to Alice's Tic Tac Toe game!")

end_game = False
last_player = ""
turn = 0

while end_game == False:
    turn += 1

    print(f"\n{t}\n")
    enter("X")
    print(f"\n{t}\n")

    if turn >= 3:
        if check_winner():
            last_player = "X"
            end_game = True
            break
    if turn == 5:
        end_game = True
        break

    enter("O")
    print(f"\n{t}\n")

    if turn >= 3:
        if check_winner():
            last_player = "O"
            end_game = True

if check_winner():
    print(f"Player {last_player} is the winner!")
else:
    print("It's a draw!")


#TODO Nuova partita? Se sì resetta la tabella

###TODO Extra: possibilità di scegliere un giocatore (user vs. computer)
