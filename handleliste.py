class Handleliste:
    def __init__(self):
        self.produkter = []

    def legg_til_produkt(self, produkt):
        self.produkter.append(produkt)

    def fjern_produkt(self, produkt):
        if produkt in self.produkter:
            self.produkter.remove(produkt)
        else:
            print(f"{produkt} er ikke i handlelisten.")

    def vis_oversikt(self):
        print("Handleliste:")
        for produkt in self.produkter:
            print(produkt)

    def lagre_handleliste(self, filnavn):
        with open(filnavn, "w") as fil:
            for produkt in self.produkter:
                fil.write(produkt + "\n")

    def laste_handleliste(self, filnavn):
        with open(filnavn, "r") as fil:
            self.produkter = [linje.strip() for linje in fil]

handleliste = Handleliste()

while True:
    print("\n1. Legg til produkt")
    print("2. Fjern produkt")
    print("3. Vis handleliste")
    print("4. Lagre handleliste")
    print("5. Last handleliste")
    print("6. Avslutt")

    valg = input("Velg en handling (1-6): ")

    if valg == "1":
        produkt = input("Skriv inn produktet du vil legge til: ")
        handleliste.legg_til_produkt(produkt)
    elif valg == "2":
        produkt = input("Skriv inn produktet du vil fjerne: ")
        handleliste.fjern_produkt(produkt)
    elif valg == "3":
        handleliste.vis_oversikt()
    elif valg == "4":
        filnavn = input("Hva vil du kalle filen: ")
        handleliste.lagre_handleliste(filnavn)
        print("Handlelisten er lagret")
    elif valg == "5":
        filnavn = input("Hva heter filen du vil laste inn: ")
        handleliste.laste_handleliste(filnavn)
        print("Handlelisten er lastet")
    elif valg == "6":
        break
    else:
        print("En feil skjedde, prøv igjen")