from bs4 import BeautifulSoup
import requests

arr = {1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023}

data_ppg = []

for elem in arr:

    url = f"https://www.statmuse.com/nba/ask/average-possessions-per-game-nba-from-{elem}"
    page = requests.get(url)

    doc = BeautifulSoup(page.text, 'html.parser')

    table = doc.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols][5]
        data_ppg.append(cols) # Get rid of empty values

def getStats():
    return data_ppg