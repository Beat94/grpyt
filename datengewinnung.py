# bevor dieses Script ausgef?hrt werden kann muss folgendes Kommando in CMD ausgef?hrt werden:
# pip install requests
# resp.
# conda install requests

import sqlite3;
import requests;
import json;
import os;
from pathlib import Path;

# Funktionen
def indikatorImport(dataIst, dataSoll, landIst, landSoll):
    print("entry: " + str(dataIst) + " / " + str(dataSoll) + "\t Land: " + str(landIst) + " / " + str(landSoll));

# variabeln definieren
countryArray = [];
dbName = "covid-db.db";

#Prüfung ob DB bereits existiert und direkte Löschung ebendieser
if Path(dbName).is_file():
    print("Datenbank " + dbName + " existiert");
    os.remove(dbName);
    quit();


# Sqlite3 DB bereitstellen
con = sqlite3.connect(dbName );
cur = con.cursor();

# Sqlite3 DB initialisieren


# request f?r L?nderabfrage
countryRequest = requests.get('https://api.covid19api.com/countries');
if(countryRequest.status_code != 200):
    quit();

# API request f?r L?nder bauen und in Array abf?llen / evt. SQLite-DB abf?llen
count = 0;
while(count < len(countryRequest.json())):
    countryArray.append(countryRequest.json()[count]);
    count = count + 1;

for element in countryArray:
    print(element['Country']);



# API request f?r covid-F?lle f?r alle l?nder abfragen und in sqlite-DB abf?llen





# sqlite3 beenden

# die ?nderungen speichern - akzeptieren - sqlite3
con.commit();

# die Verbindung schliessen - sqlite3
con.close();
