from datetime import datetime
from bs4 import BeautifulSoup
import csv
import time
import random
import requests

now = datetime.now()
timestr = now.strftime("%Y%m%d-%H%M%S")
with open('prijs'+str(timestr)+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    Spelers = {
        'Rodrigo': 198329,
        'Digne': 200458,
        'Richarlison': 231943,
        'Ousmane-dembele': 231443,
        'Sane': 222492,
        'Gabriel-jesus': 230666,
        'Adama': 213956,
        'Klostermann': 222331,
        'Sissoko': 183394,
        'Llorente': 226161,
        'Rashford': 231677,
        'Diego-carlos-santos-silva': 219693,
        'Joe gomez': 225100,
        'Militao': 240130,
        'Mendy': 228618,
        'Son': 200104,
        'Wijnaldum': 181291,
        'Havertz': 235790,
        'Valverde': 239053,
        'Mbappe': 231747,
        'Varane': 201535,
        'Donny from the River': 221363,
        'allan': 199914
    }
    ShuffledList = list(Spelers.items())
    random.shuffle(ShuffledList)
    print("Tijd van marktanalyse =", now)
    for naam, idspeler in ShuffledList:
        response = requests.get(
            'https://www.futbin.com/21/playerPrices?player='+str(idspeler))
        data = response.json()
        ValueSpeler = data[str(idspeler)]['prices']['xbox']['LCPrice']
        print(naam, ValueSpeler)
        writer.writerow([naam, ValueSpeler])
        randomNumber = random.randint(30, 60)
        time.sleep(randomNumber)

print("Klaar met zoeken")
