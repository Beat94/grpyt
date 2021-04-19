# bevor dieses Script ausgef?hrt werden kann muss folgendes Kommando in CMD ausgef?hrt werden:
# pip install requests
# resp.
# conda install requests

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
countryArray = [];
file1 = "country.csv";
file2 = "ansteckung.csv";

# csv-open
chkFileDel(file1);
table1 = open(file1, 'w');
writerTable1 = csv.writer(table1);
writerTable1.writerow(["Country", "Slug", "ISO2"]);


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
    writerTable1.writerow([count, countryRequest.json()[count]["Country"], countryRequest.json()[count]["Slug"], countryRequest.json()[count]["ISO2"]]);
    count = count + 1;




# API request f?r covid-F?lle f?r alle l?nder abfragen und in sqlite-DB abf?llen

