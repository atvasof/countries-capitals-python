#!/usr/bin/python


from bs4 import BeautifulSoup
import urllib2
from difflib import SequenceMatcher
 
wiki = "https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
 

table = soup.find("table", { "class" : "wikitable sortable" })
city=""
country=""
cities=[]
countries=[]
countries_l=[]

for row in table.findAll("tr"):
	cells = row.findAll("td")
	if len(cells) == 3:
		city = cells[0].find(text=True)
		for a in cells[1].find_all('a',title=True):
			country = a['title']
	if len(city) != 0:
		cities.append(city)
		countries.append(country)
		countries_l.append(country.lower())


while True:
	user_country =raw_input('Please enter country:' )
	user_country=user_country.lower()
	try:
		index = countries_l.index(user_country)
		print "%s is the capital of %s"%(cities[index],countries[index])
		continue
	except:
		print "this not a country"
		continue

#todo string distance










	
