from bs4 import BeautifulSoup as bs
import requests, re, itertools, csv, time
import pandas as pd

prd_name = []
prd_new_price = []
prd_old_price = []
prd_rating = []

headers = {
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
base_url = 'https://www.jumia.com.gh'
url = base_url + f'/computing/?q=laptop&page=1'
r = requests.get(url)
data = r.text
getpage = bs(data)

pattern = r'>(.*?)<'
pg_pattern = r'page=([\d]+)'
last = getpage.findAll('a', attrs={'aria-label': 'Last Page'})

try:
    max_page = re.search(pg_pattern, str(last)).group(1)
except AttributeError:
    max_page = re.search(pg_pattern, str(last))

fields = ['Product Name', 'New Price', 'Old Price', 'Rating']
filename = "laptopdata.csv"
# with open(filename, 'w', newline="", encoding='utf-8') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(fields)

def scrap_data():
    if max_page.isdigit():
        cur = 1
        while cur <= int(max_page):
            try:
                url = base_url + f'/computing/?q=pendrive&page={cur}'
                r, data, 
                webpage= bs(data)

                names = webpage.select("[class~=name]")
                new_prices = webpage.select("[class~=prc]")
                old_prices = webpage.select("[class~=old]")
                ratings = webpage.select("[class~=stars]")

                # print(new_prices, old_prices)

                for (name, new_price, old_price, rating) in itertools.zip_longest(names, new_prices, old_prices, ratings, fillvalue=0):
                    try:
                        table_namex = re.search(pattern, str(name)).group(1)
                    except AttributeError:
                        table_namex = re.search(pattern, str(name))
                    try:
                        ratingx = re.search(pattern, str(rating)).group(1)
                    except AttributeError:
                        ratingx = re.search(pattern, str(rating))

                    new_pricex =  re.findall(r'\d+', str(new_price))
                    old_pricex = re.findall(r'\d+', str(old_price))


                    # time.sleep(1)
                    prd_name.append(table_namex)
                    prd_new_price.append(''.join(new_pricex))
                    prd_old_price.append(''.join(old_pricex))
                    prd_rating.append(ratingx)
                    
                cur += 1
                print('Next page')
                # time.sleep(1)
            except ConnectionError:
                print('Check your Internet connection and Try again')
            except Exception as e:
                print('Page Ended')
                print(e)
        print('Complete')
    else:
        print('No search results for your requested items')        

scrap_data()
# time.sleep(5)
# print(getpage)

rows = zip(prd_name, prd_new_price, prd_old_price, prd_rating)

with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    # writing the fields
    writer.writerow(fields)
    for row in rows:
        writer.writerow(row)
# print(webpage.find("a", class_="pg")["aria-label"])
# print(webpage.find("a", class_="pg")["href"])

