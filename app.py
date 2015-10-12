#!/usr/bin/python


from bs4 import BeautifulSoup
import urllib2
from difflib import SequenceMatcher
from difflib import get_close_matches
from random import randint
 
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


print "\nwelcome to geografy application\n\nFor searching capital from country press 1\nFor playing the memory game press 2"

user_input=raw_input()
score=0
loops=0
while loops<100:


	if user_input=="1":
	
		user_country =raw_input('\nPlease enter country:' )
		user_country=user_country.lower()
		similar=get_close_matches(user_country,countries,1,0.7)
		try:
			index = countries_l.index(user_country)
			print "%s is the capital of %s\n"%(cities[index],countries[index])
			continue
		except:
			if len(similar)!=0:
				index = countries.index(similar[0])
				print "%s is the capital of %s\n"%(cities[index],countries[index])	
			else:
				print "This not a country"
				print "\n"

	elif user_input=="2":

		rand_index = randint(0,len(countries)-1)
		print "Score:%d/%d ,which is the capital of %s?"%(score,loops,countries[rand_index])
		user_capital =raw_input()
		similar=SequenceMatcher(None,user_capital,cities[rand_index]).ratio()
		if similar>0.55:
			score=score+1
			print "Correct %s is the capital of %s\n"%(cities[rand_index],countries[rand_index])	
		else:
			print "Wrong  %s is the capital of %s\n"%(cities[rand_index],countries[rand_index])	
			print "\n"
	loops=loops+1

print "congratulations your score is %d\nliu"%(score)
