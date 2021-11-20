import csv
import requests
from bs4 import BeautifulSoup
import pymysql

url = "http://covid19.daegu.go.kr/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find_all("p", attrs={"class": "info_variation"})
covidData = []
for covid in covids:
    columns = covid.find("em")
    covidData.append(columns.text)

print(covidData)

conn = pymysql.connect(host='localhost', user='root', password='ycdc2021', db='covid', charset='utf8')

print(type(conn))
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS deagu_covid")
cursor.execute("CREATE TABLE deagu_covid (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, newConfirmedPatient integer, newAreaOccurred integer, newOverseasOutbreak integer, completelyCured integer, gettingTreatment integer, death integer)")
cursor.execute(f"INSERT INTO deagu_covid (newConfirmedPatient, newAreaOccurred, newOverseasOutbreak, completelyCured, gettingTreatment, death) values ({covidData[0]}, {covidData[1]}, {covidData[2]}, {covidData[3]}, {covidData[4]}, {covidData[5]})")

conn.commit()
conn.close()