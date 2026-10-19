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

print(art.logo)
print("Welcome to Alice's Tic Tac Toe game!")

#TODO "Vuoi iniziare la partita?" Se sì, mantieni gioco attivo in loop fino alla fine
print(t)

#TODO Inizia il giocatore "X"; crea funzione per l'inserimento ("X" o "O")
##TODO Se riesci, migliora l'inserimento della coordinata
### Inserimento della "X"
row = int(input("Write the number of the row:"))
column = int(input("Write the number of the column:"))
t.rows[row - 1][column] = "X"
print(t)

#TODO Funzione per il calcolo se uno dei due giocatori ha vinto (se sì, fine partita e mostra vincitore)


###TODO Extra: possibilità di scegliere un giocatore (user vs. computer)
