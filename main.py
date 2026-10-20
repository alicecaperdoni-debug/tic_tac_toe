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

print(art.logo)
print("Welcome to Alice's Tic Tac Toe game!")

game_on = True
#TODO "Vuoi iniziare la partita?" Se sì, mantieni gioco attivo in loop fino alla fine
while game_on:
    print(f"\n{t}\n")
    enter("X")
    print(f"\n{t}\n")
    enter("O")
    print(f"\n{t}\n")

#TODO Funzione per il calcolo se uno dei due giocatori ha vinto (se sì, fine partita e mostra vincitore)
#TODO Nuova partita? Se sì resetta la tabella


###TODO Extra: possibilità di scegliere un giocatore (user vs. computer)
