import csv
import requests
from bs4 import BeautifulSoup
import pymysql

url = "http://covid19.daegu.go.kr/index.html"
page = requests.get(url)

filename = "covidnum.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find_all("p", attrs={"class":"info_variation"})
for covid in covids:
    columns = covid.find_all("em")
    data = [column.get_text() for column in columns]
    print(data)
    writer.writerow(data)

conn = pymysql.connect(host='localhost',
user = 'root', password='ycdc2021', db = 'covid',charset = 'utf8')

print(type(conn)) 
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS deagu_covid")
cursor.execute("CREATE TABLE deagu_covid (id text, name text, number text) values(1, '일일 확진자', 10")

conn.commit()
conn.close()