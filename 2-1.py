import csv
import requests
from bs4 import BeautifulSoup
import pymysql

url = "https://gb.go.kr/corona_main.htm"
page = requests.get(url)

#filename = "covidnum.csv"
#f = open(filename, "w", encoding="utf-8-sig", newline="")
#writer = csv.writer(f)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find("div", attrs={"class": "count_vaccine"}).find("tbody").find_all("tr")
for covid in covids:
    columns = covid.find_all("td")
    data = [column.get_text().strip() for column in columns]
    print(data)