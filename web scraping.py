#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
#step1-- Get the HTML
content = requests.get(url)
htmlContent = content.content
#print(htmlcontent)
#step2-- Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#step3-- HTML Tree traversal
#Step 4-- comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
exit()

#get the title of the HTML page
title = soup.title
print(title.string)
print(type(soup))
print(type(title))
print(type(title.string)) 
# Get all the paragraph from the page
paras = soup.find_all('p')
#print(paras)
anchors = soup.find_all('a')
#print(anchors)
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))
print(soup.find('p').get_text())
#print(soup.get_text())
# Get all the anchor tags from the page
all_links = set()
for link in anchors:
	if(link.get('href') != '#'):
		linkText = "https://codewithharry.com" +link.get('href')
		all_links.add(link)
	print(linkText)