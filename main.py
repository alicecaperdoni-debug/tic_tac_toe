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
    row = int(input("Write the number of the row:"))
    column = int(input("Write the number of the column:"))
    global t
    t.rows[row - 1][column] = f"{player}"

print(art.logo)
print("Welcome to Alice's Tic Tac Toe game!")

#TODO "Vuoi iniziare la partita?" Se sì, mantieni gioco attivo in loop fino alla fine
print(t)

enter("X")
print(t)
enter("O")
print(t)

#TODO Funzione per il calcolo se uno dei due giocatori ha vinto (se sì, fine partita e mostra vincitore)


###TODO Extra: possibilità di scegliere un giocatore (user vs. computer)
