from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 100)  # Árakat meg lehet változtatni

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 150)  # Árakat meg lehet változtatni

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        return None

    def lemondas(self, datum):
        for foglalas in self.foglalasok:
            if foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# Szálloda létrehozása
szalloda = Szalloda("Példa Szálloda")

# Szobák hozzáadása
szalloda.add_szoba(EgyagyasSzoba("101"))
szalloda.add_szoba(KetagyasSzoba("201"))
szalloda.add_szoba(KetagyasSzoba("202"))

# Foglalások hozzáadása
szalloda.foglalas("101", datetime(2024, 5, 10))
szalloda.foglalas("201", datetime(2024, 5, 12))
szalloda.foglalas("202", datetime(2024, 5, 15))
szalloda.foglalas("101", datetime(2024, 5, 18))
szalloda.foglalas("201", datetime(2024, 5, 20))

# Felhasználói interfész és adatvalidáció
while True:
    print("\nVálasszon egy műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Művelet kiválasztása: ")

    if valasztas == "1":
        szobaszam = input("Adja meg a szobaszámot: ")
        datum_input = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_input, "%Y-%m-%d")
            if datum < datetime.now():
                print("Hibás dátum! Csak jövőbeli foglalás lehetséges.")
            else:
                ar = szalloda.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"Sikeres foglalás! Ár: {ar}")
                else:
                    print("Nincs ilyen szobaszám.")
        except ValueError:
            print("Hibás dátumformátum!")

    elif valasztas == "2":
        datum_input = input("Adja meg a lemondás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_input, "%Y-%m-%d")
            if szalloda.lemondas(datum):
                print("Sikeres lemondás.")
            else:
                print("Nincs ilyen foglalás ezen a dátumon.")
        except ValueError:
            print("Hibás dátumformátum!")

    elif valasztas == "3":
        print("Összes foglalás:")
        szalloda.listaz_foglalasok()

    elif valasztas == "4":
        break

    else:
        print("Érvénytelen választás! Kérem, válasszon újra.")
