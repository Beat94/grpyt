# bevor dieses Script ausgef?hrt werden kann muss folgendes Kommando in CMD ausgeführt werden:
# pip install requests
# resp.
# conda install requests

import time;
import csv;
import requests;
import json;
import os;
from pathlib import Path;

# Funktionen
def indikatorImport(dataIst, dataSoll, landIst, landSoll):
    print("entry: " + str(dataIst) + " / " + str(dataSoll) + "\t Land: " + str(landIst) + " / " + str(landSoll));

def chkFileDel(fileN):
    if Path(fileN).is_file():
        print("File " + fileN + " existiert");
        os.remove(fileN);
        print("File geloescht");

# variabeln definieren
file1 = "country.csv";
file2 = "ansteckung.csv";

# csv-open
chkFileDel(file1);
table1 = open(file1, 'w');
writerTable1 = csv.writer(table1);
writerTable1.writerow(["Country", "Slug", "ISO2"]);

chkFileDel(file2);
table2 = open(file2, 'w');
writerTable2 = csv.writer(table2);
writerTable2.writerow(["Country", "CountryCode", "Province", "City", "Lat", "Lon", "Confirmed", "Deaths", "Recovered", "Active", "Date"]);


# request für Länderabfrage
countryRequest = requests.get('https://api.covid19api.com/countries');
if(countryRequest.status_code != 200):
    print("connection zu der API gefailed")
    quit();

# API request für Länder bauen und in Array abf?llen / evt. SQLite-DB abfüllen
count = 0;
while(count < len(countryRequest.json())):
    print(countryRequest.json()[count]["Country"] + "\t" + countryRequest.json()[count]["Slug"] + "\t" + countryRequest.json()[count]["ISO2"]);
    writerTable1.writerow([count, countryRequest.json()[count]["Country"], countryRequest.json()[count]["Slug"], countryRequest.json()[count]["ISO2"]]);
    count = count + 1;

# API request für covid-Fälle für alle Länder abfragen und in sqlite-DB abfüllen
count = 0;
while(count < len(countryRequest.json())):
    fallRequest = requests.get('https://api.covid19api.com/country/' + countryRequest.json()[count]["Country"]);
    if(fallRequest.status_code != 200):
        print("Connection zu API 2 gefailed");
        quit();
    
    count1 = 0
    while(count1 < len(fallRequest.json())):
        writerTable2.writerow([fallRequest.json()[count1]["Country"], fallRequest.json()[count1]["CountryCode"], fallRequest.json()[count1]["Province"], fallRequest.json()[count1]["City"], fallRequest.json()[count1]["Lat"], fallRequest.json()[count1]["Lon"], fallRequest.json()[count1]["Confirmed"], fallRequest.json()[count1]["Deaths"], fallRequest.json()[count1]["Recovered"], fallRequest.json()[count1]["Active"], fallRequest.json()[count1]["Date"]]);
        indikatorImport(count, len(countryRequest.json()), count1, len(fallRequest.json()));
        count1 = count1 + 1;
    time.sleep(10)
    count = count + 1;

