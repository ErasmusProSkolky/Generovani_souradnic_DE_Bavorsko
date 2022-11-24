Generování souřadnic

    soubor: souradnice_skolky_DE_Bavorsko.py
    
    vstup: seznam_skolky_Bavorsko.csv
    
    výstup: DE_Bavorsko_povedene_MS.csv, DE_Bavorsko_nepovedene.csv
			
Extrakce adres z nepovedených 
   
    soubor: pouze_adresy_nepovedene.py
    
    vstup: DE_Bavorsko_nepovedene.csv
    
    výstup: adresy_nepovedene_pro_gpsvizualizer.csv

Extrakce souřadnic ze soubou vygenerovaného Gpsvizualizer, uložení souřadnic do jednotlivých řádků v DE_Bavorsko_nepovedene.csv a následné uložení původně nepovedených adres do  DE_Bavorsko_povedene_MS.csv
    
    soubor: uprava_nepovedene_adresy.py
    
    vstup: adresy_z_gpsvizualizer.csv, DE_Bavorsko_nepovedene.csv
    
    výstup: DE_Bavorsko_povedene_MS.csv - obohacený o nové řádky
