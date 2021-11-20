import csv
import requests
from bs4 import BeautifulSoup

url = "http://covid19.daegu.go.kr/index.html"
page = requests.get(url)

filename = "코로나현황.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find("div", attrs={"class":"status_area"}).find_all("ul")
for covid in covids:
    columns = covid.find_all("li")
    data = [column.get_text() for column in columns]
    writer.writerow(data)