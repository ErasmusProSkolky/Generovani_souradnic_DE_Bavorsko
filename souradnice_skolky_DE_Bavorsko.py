# import modulu geopy 
from geopy.geocoders import Nominatim
 
# načtení the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# otevření souboru
with open('seznam_skolky_Bavorsko.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# vytvoření seznamu z jednoho řádku
jeden_radek = [radek.split('\n') for radek in radky]

# proměnné pro ukládání 
nepovedene = []
povedene = []

# generování souřadnic - povedené se ukládají do jednoho souboru a nepovedené do jiného
for cast_radku in jeden_radek[1:]:
    try:
        # rozdělení řádku na jednotlivé údaje
        cast = cast_radku[0].split(";")
                
        # načtení adresy
        adresa = cast[7] + ', ' + cast[9]
        getLoc = loc.geocode(adresa)
        
        # vypsání adresy a souřadnic (pouze pro kontrolu, že se generují)
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)

        # uložení potřebných údajů do proměnné povedené
        data = ""
        nazev = cast[2] + ' ' + cast[3]
        skolka = nazev + ";" + adresa + ";" + cast[14] + ";" + cast[12] + ";" + cast[16]
        data+=skolka
        povedene.append(skolka + ";" + str(getLoc.latitude) + ";" + str(getLoc.longitude) + "\n")
    except Exception as chyba:
        # uložení potřebných údajů do proměnné nepovedené
        data_nepov = ""
        skolka_nepov = nazev + ";" + adresa + ';' + cast[14] + ";" + cast[12] + ";" + cast[16]
        data_nepov+=skolka_nepov
        nepovedene.append(data_nepov + ";" +"\n")
        pass

# vložení hlavičky u povedených
hlavicka = "NAZEV" + ";" + "ADRESA" + ";" + "KAPACITA" + ";" + "WEB" + ";" + "AKTUALNI_OBSAZENOST" + ";" + "LATITUDE" + ";" + "LONGITUDE" + "\n"
povedene.insert(0,hlavicka)
#print(povedene)

# uložení povedených do souboru
with open("DE_Bavorsko_povedene_MS.csv", "w", encoding="utf-8") as vystup:
    vystup.writelines(povedene)

# uložení nepovedených do souboru
with open("DE_Bavorsko_nepovedene.csv", "w", encoding="utf-8") as soubor:
    soubor.writelines(nepovedene)
