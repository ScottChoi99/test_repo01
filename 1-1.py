import csv
import requests
from bs4 import BeautifulSoup

url = "https://gb.go.kr/corona_main.htm"
page = requests.get(url)

filename = "covidnum1.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

soup = BeautifulSoup(page.content, 'html.parser')
covids = soup.find_all("div", attrs={"class": "corona_count"})
print(covids)
