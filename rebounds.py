from bs4 import BeautifulSoup
import requests

arr = {1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007}

data_rebounds = []

for elem in arr:

    url = f"https://www.statmuse.com/nba/ask/league-average-usage-rate-{elem}-by-position"
    page = requests.get(url)

    doc = BeautifulSoup(page.text, 'html.parser')

    table = doc.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols][6]
        data_rebounds.append(cols) # Get rid of empty values

def getStats():
    return data_rebounds