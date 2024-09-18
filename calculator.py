# bau mir eine einfache taschenrechner funktionalität mit addieren und subtrahieren

# Eingabe

#Funktionsaufruf
def errechne_summe(n, m):
    errechnete_summe = n + m
    return errechnete_summe

def errechne_differenz(n, m):
    errechnete_differenz = n - m
    return errechnete_differenz

#Funktionsaufruf
if __name__ == "__main__":
    n = int(input("Gib eine Zahl ein: "))
    m = int(input("Gib eine weitere Zahl ein: "))
    print(errechne_summe(n, m))
    print(errechne_differenz(n, m))