import urllib
import requests
import bs4

home_page = 'https://www.ikea.com'


""" *******************************************************************
						
						Begin grabbing beds
						
*********************************************************************"""

beds_links_manual = ["https://www.ikea.com/ae/en/catalog/categories/departments/bedroom/16284/",
"https://www.ikea.com/ae/en/catalog/categories/departments/bedroom/16285/",
"https://www.ikea.com/ae/en/catalog/categories/departments/bedroom/28433/",
"https://www.ikea.com/ae/en/catalog/categories/departments/bedroom/25205/",
"https://www.ikea.com/ch/en/catalog/categories/departments/bedroom/16284/",
"https://www.ikea.com/ch/en/catalog/categories/departments/bedroom/28433/",
"https://www.ikea.com/ch/en/catalog/categories/departments/bedroom/16285/",
"https://www.ikea.com/es/en/catalog/categories/departments/bedroom/16284/",
"https://www.ikea.com/es/en/catalog/categories/departments/bedroom/16285/",
"https://www.ikea.com/es/en/catalog/categories/departments/bedroom/19037/",
"https://www.ikea.com/es/en/catalog/categories/departments/bedroom/25205/",
"https://www.ikea.com/kw/en/catalog/categories/departments/bedroom/16284/",
"https://www.ikea.com/kw/en/catalog/categories/departments/bedroom/16285/",
"https://www.ikea.com/sa/en/catalog/categories/departments/bedroom/16284",
"https://www.ikea.com/sa/en/catalog/categories/departments/bedroom/16285",
"https://www.ikea.com/sa/en/catalog/categories/departments/bedroom/28433",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/16284/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/16285/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/25205/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/19037/"]

i=0
for link in chairs_links_manual:
	conn = requests.get(link)
	conn_bs4 = bs4.BeautifulSoup(conn.text,'html5lib')
	conn_imgs = conn_bs4.select('.prodImg')
	for imgs in conn_imgs:
		#print imgs['src']
		print (home_page+imgs['src'])
		imageNaME=imgs['src'].split(".")
		imageNaME=imageNaME[len(imageNaME)-2].split("/")
		print ((imageNaME[len(imageNaME)-1])+".jpg")
		urllib.urlretrieve(home_page+imgs['src'],("chairs/"+imageNaME[len(imageNaME)-1])+".jpg")
		i+=1


""" *******************************************************************
						
						End of grabbing beds
						
*********************************************************************"""



""" *******************************************************************
						
						Begin grabbing chairs	
						
*********************************************************************"""


chairs_links_manual = ["https://www.ikea.com/ae/en/catalog/categories/departments/living_room/16239/",
"https://www.ikea.com/es/en/catalog/categories/departments/childrens_ikea/18715/",
"https://www.ikea.com/es/en/catalog/categories/departments/childrens_ikea/18733/",
"https://www.ikea.com/es/en/catalog/categories/departments/workspaces/20652/",
"https://www.ikea.com/es/en/catalog/categories/departments/dining/25219/",
"https://www.ikea.com/es/en/catalog/categories/departments/outdoor/21966/",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/16239/",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/25219",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/20864",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/18733",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/16239",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/20652",
"https://www.ikea.com/us/en/catalog/categories/departments/living_room/16239/",
"https://www.ikea.com/us/en/catalog/categories/departments/dining/25219/",
"https://www.ikea.com/us/en/catalog/categories/departments/dining/18733/"
]


i=0
for link in chairs_links_manual:
	conn = requests.get(link)
	conn_bs4 = bs4.BeautifulSoup(conn.text,'html5lib')
	conn_imgs = conn_bs4.select('.prodImg')
	for imgs in conn_imgs:
		#print imgs['src']
		print (home_page+imgs['src'])
		imageNaME=imgs['src'].split(".")
		imageNaME=imageNaME[len(imageNaME)-2].split("/")
		print ((imageNaME[len(imageNaME)-1])+".jpg")
		urllib.urlretrieve(home_page+imgs['src'],("chairs/"+imageNaME[len(imageNaME)-1])+".jpg")
		i+=1
		

""" *******************************************************************
						
						End of grabbing chairs
						
*********************************************************************"""

""" *******************************************************************
						
						Begin grabbing lights
						
*********************************************************************"""



lights_links_manual = ["https://www.ikea.com/es/en/catalog/categories/departments/lighting/20502/",
"https://www.ikea.com/es/en/catalog/categories/departments/lighting/10732/",
"https://www.ikea.com/es/en/catalog/categories/departments/lighting/10731/",
"https://www.ikea.com/es/en/catalog/categories/departments/lighting/18750/",
"https://www.ikea.com/es/en/catalog/categories/departments/lighting/20503/",
"https://www.ikea.com/es/en/catalog/categories/departments/lighting/10736/",
"https://www.ikea.com/es/en/catalog/categories/departments/living_room/10744/",
"https://www.ikea.com/sa/en/catalog/categories/departments/lighting/10731",
"https://www.ikea.com/sa/en/catalog/categories/departments/lighting/10732",
"https://www.ikea.com/sa/en/catalog/categories/departments/lighting/20502",
"https://www.ikea.com/sa/en/catalog/categories/departments/lighting/20503",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/10731/",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/20503/",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/10744/",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/10732/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/10732/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/20503/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/18750/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/36812/",
"https://www.ikea.com/us/en/catalog/categories/departments/bedroom/10731/",
"https://www.ikea.com/us/en/catalog/categories/departments/living_room/20515/",
"https://www.ikea.com/us/en/catalog/categories/departments/living_room/20503/"
]


i=0
for link in lights_links_manual:
	conn = requests.get(link)
	conn_bs4 = bs4.BeautifulSoup(conn.text,'html5lib')
	conn_imgs = conn_bs4.select('.prodImg')
	for imgs in conn_imgs:
		#print imgs['src']
		print (home_page+imgs['src'])
		imageNaME=imgs['src'].split(".")
		imageNaME=imageNaME[len(imageNaME)-2].split("/")
		print ((imageNaME[len(imageNaME)-1])+".jpg")
		urllib.urlretrieve(home_page+imgs['src'],("lights/"+imageNaME[len(imageNaME)-1])+".jpg")
		i+=1
		
		
""" *******************************************************************
						
						End of grabbing lights
						
*********************************************************************"""



""" *******************************************************************
						
						Begin grabbing tables	
						
*********************************************************************"""

tables_links_manual = ["https://www.ikea.com/es/en/catalog/categories/departments/bedroom/20656/",
"https://www.ikea.com/es/en/catalog/categories/departments/dining/16244/",
"https://www.ikea.com/es/en/catalog/categories/departments/workspaces/desks_and_tables/",
"https://www.ikea.com/es/en/catalog/categories/departments/living_room/10705/",
"https://www.ikea.com/es/en/catalog/categories/departments/dining/21825/",
"https://www.ikea.com/es/en/catalog/categories/departments/outdoor/21962/",
"https://www.ikea.com/es/en/catalog/categories/departments/outdoor/21965/",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/21825",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/10705",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/18701",
"https://www.ikea.com/sa/en/catalog/categories/departments/dining/21965",
"https://www.ikea.com/us/en/catalog/categories/departments/living_room/10705/",
"https://www.ikea.com/us/en/catalog/categories/departments/living_room/10475/",
"https://www.ikea.com/us/en/catalog/categories/departments/dining/21825/",
"https://www.ikea.com/kw/en/catalog/categories/departments/living_room/10705/"]

i=0
for link in tables_links_manual:
	conn = requests.get(link)
	conn_bs4 = bs4.BeautifulSoup(conn.text,'html5lib')
	conn_imgs = conn_bs4.select('.prodImg')
	for imgs in conn_imgs:
		#print imgs['src']
		print (home_page+imgs['src'])
		imageNaME=imgs['src'].split(".")
		imageNaME=imageNaME[len(imageNaME)-2].split("/")
		print ((imageNaME[len(imageNaME)-1])+".jpg")
		urllib.urlretrieve(home_page+imgs['src'],("tables/"+imageNaME[len(imageNaME)-1])+".jpg")
		i+=1


""" *******************************************************************
						
						End of grabbing tables
						
*********************************************************************"""

