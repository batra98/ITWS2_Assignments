import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.amazon.in/gp/bestsellers/books/'
page = requests.get(url)


soup = BeautifulSoup(page.content, "lxml")

listwebpages = []
for items in (soup.find_all("li", {"class": "zg_page zg_selected"})):
    listwebpages.append(items.find('a')['href'])


for items in (soup.find_all("li", {"class": "zg_page "})):
    listwebpages.append(items.find('a')['href'])


temp = []
pages = []

for items in listwebpages:
    temp.append(requests.get(items))

for items in temp:
    pages.append(BeautifulSoup(items.content, "lxml"))


url_final = []
name_final = []
listing = []


temp1 = []

for k in range(5):
    temp1.append(pages[k].find_all('div', {'class': 'zg_itemWrapper'}))

for g in range(len(temp1)):
    for books in temp1[g]:
        listing.append(books.find_all("div"))

j = 0


for i in range(len(listing)):
    try:
        url_final.append(listing[i][j].find('a')['href'])
    except:
        url_final.append("Not Available")


j = 2

for i in range(len(listing)):
    try:
        name_final.append(listing[i][j].contents)
    except:
        name_final.append("Not Available")

j = 3
author_final = []


for i in range(len(listing)):
    try:
        author_final.append(listing[i][j].find('a').contents)
    except:
        author_final.append(listing[i][j].find('span').contents)


j = 4
stars_final = []

for i in range(len(listing)):

    try:
        stars_final.append(listing[i][j].find(
            'a').find('i').find('span').contents)
    except AttributeError:

        stars_final.append(listing[i][3].find(
            'a').find('i').find('span').contents)
    except:
        stars_final.append(["Not Available"])


temp3 = []
rating_final = []
for i in (listing):

    try:
        rating_final.append(
            list(i[j].find_all('a', {'class': 'a-size-small a-link-normal'}))[0].contents)
    except IndexError:
        rating_final.append(
            list(i[j-1].find_all('a', {'class': 'a-size-small a-link-normal'}))[0].contents)

    except:
        rating_final.append(["Not Available"])


j = 6

price_final = []


for i in range(len(listing)):
    try:
        price_final.append(list(listing[i][j].find(
            'a').find('span').find('span').contents)[1])
    except:
        price_final.append("Not Available")


name_final = [x[0].strip() for x in name_final]

url_final = ["https://www.amazon.com"+x for x in url_final]
author_final = [x[0].strip() for x in author_final]

rating_final = [x[0] for x in rating_final]
stars_final = [x[0] for x in stars_final]

final = [name_final, url_final, author_final,
         price_final, rating_final, stars_final]
final = list(zip(*final))


myFile = open('./output/in_books.csv', 'w')
csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_ALL)
with myFile:
    writer = csv.writer(myFile, dialect='myDialect')

    writer.writerow(["Name", "URL", "Author", "Price",
                     "Ratings", "Average Ratings"])
    writer.writerows(final)
