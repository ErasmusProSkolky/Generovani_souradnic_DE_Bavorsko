# načtení souboru
with open ('DE_Bavorsko_nepovedene.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# oddělení řádků
radek = [radek.split('\n') for radek in radky]
udaje = [udaj[0].split(';') for udaj in radek]

# vybrání adres a uložení do proměnné
adresy = []
for udaj in udaje:
    adresa = udaj[1]
    adresy.append(adresa + '\n')

with open('adresy_nepovedene_pro_gpsvizualizer.csv', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(adresy)

