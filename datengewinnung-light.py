import time;
import csv;
import requests;
import json;
import os;
from pathlib import Path;

# Funktionen
def indikatorImport(dataIst, dataSoll, landIst, landSoll):
    print("Land: " + str(dataIst) + " / " + str(dataSoll) + "\t Entry: " + str(landIst) + " / " + str(landSoll));

def chkFileDel(fileN):
    if Path(fileN).is_file():
        print("File " + fileN + " existiert");
        os.remove(fileN);
        print("File geloescht");

# variablen definieren
file1 = "country.csv";
file2 = "ansteckung.csv";
sleepCount = 20;
countries = [];

# csv-open
if Path(file1).is_file():
    print("File1 existiert");
    with open(file1, 'r') as file:
        for row in csv.reader(file):
            print(row[0]);
            countries.append(row[0]);
else:
    print("File1 existiert nicht bitte File noch anf?gen");
    quit();


chkFileDel(file2);
table2 = open(file2, 'w');
writerTable2 = csv.writer(table2);
writerTable2.writerow(["Country", "CountryCode", "Province", "City", "Lat", "Lon", "Confirmed", "Deaths", "Recovered", "Active", "Date"]);

count = 0;
while(count < len(countries)):
    fallRequest = requests.get('https://api.covid19api.com/country/' + countries[count]);
    if(fallRequest.status_code != 200):
        print("Connection zu API 2 gefailed " + str(count));
        sleepCount = sleepCount + 5;
    else:
        count1 = 0
        while(count1 < len(fallRequest.json())):
            writerTable2.writerow([fallRequest.json()[count1]["Country"], fallRequest.json()[count1]["CountryCode"], fallRequest.json()[count1]["Province"], fallRequest.json()[count1]["City"], fallRequest.json()[count1]["Lat"], fallRequest.json()[count1]["Lon"], fallRequest.json()[count1]["Confirmed"], fallRequest.json()[count1]["Deaths"], fallRequest.json()[count1]["Recovered"], fallRequest.json()[count1]["Active"], fallRequest.json()[count1]["Date"]]);
            indikatorImport(count, len(countries), count1, len(fallRequest.json()));
            count1 = count1 + 1;
        count = count + 1;
    time.sleep(sleepCount);
