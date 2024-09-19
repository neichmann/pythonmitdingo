# bau mir ein simples skript, das gut aufzeigt, warum funktionale programmierung sinnvoll ist

# Das Problem ist dass du eine Funktion bauen willst,
# die die Summe aller Zahlen bis zu einer Zahl n addiert
def berechne_summe(n):
    errechnete_summe = 0
    for i in range(1, n):
        errechnete_summe = errechnete_summe + i
    return errechnete_summe



if __name__ == "__main__":
    # Eingabe
    n = int(input("Gib eine Zahl ein: "))
    #Funktionsaufruf
    ergebnis = berechne_summe(n)
    # ergebnis quadrieren
    ergebnis = ergebnis * ergebnis
    print(f"Die Summe der Zahlen von 1 bis {n} ist: {ergebnis}")