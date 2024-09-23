import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://yugiohtopdecks.com/decks/Orcust"
toss_start = datetime.strptime("07/15/2019", "%m/%d/%Y")

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("table", class_="sortable")

print(results)