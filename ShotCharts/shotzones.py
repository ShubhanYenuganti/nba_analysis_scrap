from bs4 import BeautifulSoup
import requests

url = "https://www.nba.com/stats/players/shooting?PlayerPosition=F&Season=2022-23&PerMode=Totals&DistanceRange=By+Zone"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

results = soup.find_all("tr")

for result in results:
    print(result)
    print()
    print()