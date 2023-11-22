from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://www.bbc.com/ukrainian/features-66330880'

response = requests.get(url)
if response.status_code ==200:
    bs = BeautifulSoup(response.text, features='html.parser')
    list = bs.find_all('h2')
    for elem in list[:10]:
        title=elem.text
#        print(title)

conection = sqlite3.connect("Ispit_DB.sl3", 5)
cur = conection.cursor()
cur.execute("SELECT rowid, name FROM less12 WHERE rowid=6")
rez = cur.fetchall()
print(rez)
conection.commit()
