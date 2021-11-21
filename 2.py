import csv
import requests
from bs4 import BeautifulSoup
import pymysql

url = "http://covid19.daegu.go.kr/index.html"
page = requests.get(url)

#filename = "covidnum.csv"
#f = open(filename, "w", encoding="utf-8-sig", newline="")
#writer = csv.writer(f)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find("tbody").find_all("tr")
for covid in covids:
    columns = covid.find_all("td")
    data = [column.get_text() for column in columns]
    print(data)