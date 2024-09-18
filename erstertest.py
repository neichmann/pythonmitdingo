# Das Problem ist dass du eine Funktion bauen willst,
# die die Summe aller Zahlen bis zu einer Zahl n addiert
def berechne_summe(n):
    errechnete_summe = 0
    for i in range(0, n+1):
        errechnete_summe = (errechnete_summe + i)
    return errechnete_summe

def say_my_name(name):
    print(name)

if __name__ == "__main__":
    # Eingabe
    n = int(input("Gib eine Zahl ein: "))
    #Funktionsaufruf
    ergebnis = berechne_summe(n)
    summenergebnis = berechne_summe(ergebnis)
    print(f"Die Summe der Zahlen von 1 bis {n} ist: {summenergebnis}")
    for i in range(1, 6):
        print(i)
    name = str(input("Name: "))
    say_my_name(name)
