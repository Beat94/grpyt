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

#Pr?fung ob DB bereits existiert und direkte L?schung ebendieser
if Path(dbName).is_file():
    print("Datenbank " + dbName + " existiert");
    os.remove(dbName);
    print("Datenbank entfernt");
    #quit();


# Sqlite3 DB bereitstellen
con = sqlite3.connect(dbName);
print("Datenbank erstellt");
cur = con.cursor();

# Sqlite3 DB initialisieren
cur.execute("create table tbl_country (ISO2 varchar(255), Country varchar(255), Slug varchar(255))");
print("tbl_country ist erstellt");
cur.execute("create table tbl_daten (Country varchar(255), CountryCode varchar(255), Province varchar(255), City varchar(255), CityCode varchar(255), lat varchar(255), lon varchar(255), Confirmed int, Deaths int, Recovered int, Active int, date varchar(255))");
print("tbl_daten erstellt");


# request f?r L?nderabfrage
countryRequest = requests.get('https://api.covid19api.com/countries');
if(countryRequest.status_code != 200):
    print("connection zu der API gefailed")
    quit();

# API request f?r L?nder bauen und in Array abf?llen / evt. SQLite-DB abf?llen
count = 0;
while(count < len(countryRequest.json())):
    countryArray.append(countryRequest.json()[count]);
    print(countryRequest.json()[count]["Country"] + "\t" + countryRequest.json()[count]["Slug"] + "\t" + countryRequest.json()[count]["ISO2"]);
    cur.execute("insert into tbl_country (ISO2, Country, Slug) values (" + str(countryRequest.json()[count]["ISO2"]) + ", " + str(countryRequest.json()[count]["Country"]) + ", " + str(countryRequest.json()[count]["Slug"]) + ")");
    count = count + 1;

#for element in countryArray:
    #print(element['Country']);
    #print(count)



# API request f?r covid-F?lle f?r alle l?nder abfragen und in sqlite-DB abf?llen





# sqlite3 beenden

# die ?nderungen speichern - akzeptieren - sqlite3
con.commit();

# die Verbindung schliessen - sqlite3
con.close();
