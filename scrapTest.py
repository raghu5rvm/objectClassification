import urllib
import requests
import bs4

home_page = 'https://www.ikea.com/'




country_link_raw = requests.get(home_page)

country_link_bs4 = bs4.BeautifulSoup(country_link_raw.text,'html5lib')

country_link_final = country_link_bs4.select('.country-selection__single-lang > a')

country_linkM_final = country_link_bs4.select('.country-selection__multi-lang > ul > li > a')

country_link_final += country_linkM_final

print len(country_link_final)

for link in country_link_final:
	
	if(link['data-languagecode']=='EN'):
			print link['href']








