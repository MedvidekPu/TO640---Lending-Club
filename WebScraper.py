import csv
from urllib.request import urlopen
from html import unescape
from time import sleep

# Scrape 50 pages in defined URL
pages = []
for page in range(1,51):
    url = 'http://books.toscrape.com/catalogue/page-'+str(page)+'.html'
    siteAsString = urlopen(url).read().decode()
    pages.append(siteAsString)

# Split every page into books by using <h3> and save it in separate list
pages_books = []
for page in pages:
    book = page.split('<h3>') #define book category
    pages_books.append(book)
    #sleep(2) # Sleep is mostly not needed as the pages load fast enough

# Create new file Product.csv, go through every book and every page, specify the position of title and price in the book and write in in csv file.
# The newline='' makes sure that we do not create empty row with every new entry, the specified encoding was needed to correctly read the names of the books
with open('Product.csv', 'w', encoding="utf-8-sig", newline='') as f_out: 
    writer = csv.writer(f_out)
    writer.writerow(["Title", "Price"])
    for page in pages_books:
        for book in page[1:]:
            title_start=book.find('title="')
            title_end=book.find(">")
            price_start=book.find('<p class="price_color">')
            price_end=book.find('</p>')
            
            row_title=book[title_start+len('title="'):title_end]
            row_price=book[price_start+(len('<p class="price_color">')+1):price_end]
            
            #write title and price
            row_title = unescape(row_title.strip().replace('"',''))
            row_price = unescape(row_price.strip())
            writer.writerow([row_title, row_price])

