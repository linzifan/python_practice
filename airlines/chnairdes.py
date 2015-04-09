# coding: utf-8
import requests
from bs4 import BeautifulSoup
import csv


url_dic = {"CA.csv":"http://en.wikipedia.org/wiki/Air_China_destinations",
           "MU.csv":"http://en.wikipedia.org/wiki/China_Eastern_Airlines_destinations",
           "CZ.csv":"http://en.wikipedia.org/wiki/China_Southern_Airlines_destinations",
           "HU.csv":"http://en.wikipedia.org/wiki/Hainan_Airlines_destinations"}

for item in url_dic.items():
    # get url
    url = item[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    alltables = soup.findAll('table')
    # Identify the table of destinations
    # table has the structure: City | Province | Country | IATA | ICAO | Airport
    for i in range(len(alltables)):
        try:
            if alltables[i].findAll('th')[0].get_text() == "City":
                break
        except:
            continue
    # write csv
    with open(item[0],'wb') as f:
        filewriter = csv.writer(f, delimiter = ',')
        filewriter.writerow(["City", "Country", "IATA", "ICAO", "Airport"])
        for row in alltables[i].findAll('tr'):
            try:
                city = row.findAll('td')[0].get_text().splitlines()[0]
                country = row.findAll('td')[2].get_text()
                iata = row.findAll('td')[3].get_text()
                icao = row.findAll('td')[4].get_text()
                airport = row.findAll('td')[5].get_text()
                filewriter.writerow([city, country, iata, icao, airport])
            except:
                continue
    f.close()
    print item[0] + " has been created."
