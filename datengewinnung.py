# bevor dieses Script ausgef�hrt werden kann muss folgendes Kommando in CMD ausgef�hrt werden:
# pip install requests
# resp.
# conda install requests

import sqlite3;
import requests;

# Sqlite3 DB bereitstellen
con = sqlite3.connect('covid-db.db');
cur = con.cursor();

# requests initialisieren


# API request f�r L�nder bauen und in Array abf�llen / evt. SQLite-DB abf�llen




# API request f�r covid-F�lle f�r alle l�nder abfragen und in sqlite-DB abf�llen





# sqlite3 beenden

# die �nderungen speichern - akzeptieren - sqlite3
con.commit();

# die Verbindung schliessen - sqlite3
con.close();
