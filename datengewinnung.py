# bevor dieses Script ausgeführt werden kann muss folgendes Kommando in CMD ausgeführt werden:
# pip install requests
# resp.
# conda install requests

import sqlite3;
import requests;

# Sqlite3 DB bereitstellen
con = sqlite3.connect('covid-db.db');
cur = con.cursor();

# requests initialisieren


# API request für Länder bauen und in Array abfüllen / evt. SQLite-DB abfüllen




# API request für covid-Fälle für alle länder abfragen und in sqlite-DB abfüllen





# sqlite3 beenden

# die änderungen speichern - akzeptieren - sqlite3
con.commit();

# die Verbindung schliessen - sqlite3
con.close();
