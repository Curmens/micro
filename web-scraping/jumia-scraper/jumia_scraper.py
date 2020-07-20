from bs4 import BeautifulSoup as bs
import requests, re, itertools, csv, time
import pandas as pd


prd_name = []
prd_new_price = []
prd_old_price = []
prd_rating = []
rest = time.sleep

searchItem = input('Enter Item to get data: ').replace(' ', '+')

start_time = time.time()

headers = {
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
base_url = 'https://www.jumia.com.gh'
url = base_url + f'/catalog/?q={searchItem}&page=1'
r = requests.get(url)
data = r.text
getpage = bs(data, features="html5lib")

pattern = r'>(.*?)<'
pg_pattern = r'page=([\d]+)'
last = getpage.findAll('a', attrs={'aria-label': 'Last Page'})

try:
    max_page = re.search(pg_pattern, str(last)).group(1)
except AttributeError:
    max_page = re.search(pg_pattern, str(last))

fields = ['Product Name', 'New Price', 'Old Price', 'Rating']
filename = f"{searchItem}_data.csv"

def scrap_data():
    if max_page.isdigit():
        cur = 1
        while cur <= int(max_page):
            try:
                url = base_url + f'/catalog/?q={searchItem}&page={cur}'
                r = requests.get(url).text
                webpage = bs(r, features="html5lib")

                names = webpage.select("[class~=name]")
                new_prices = webpage.select("[class~=prc]")
                old_prices = webpage.select("[class~=old]")
                ratings = webpage.select("[class~=stars]")


                print(f'Page {cur} of {max_page}')
                cur += 1

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


                    prd_name.append(table_namex)
                    prd_new_price.append(''.join(new_pricex))
                    prd_old_price.append(''.join(old_pricex))
                    prd_rating.append(ratingx)

            except ConnectionError or ConnectionResetError:
                print('Check your Internet connection and Try again')
            except Exception as e:
                print('Page Has Been Closed By Host Check Your Internet Connection.....')
        print('Scraping Has Completed Successfully [...]')
    else:
        print('No search results for your requested items')        

scrap_data()

rows = zip(prd_name, prd_new_price, prd_old_price, prd_rating)
rest(2)
print('Extracting Data to File [...]')

with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    # writing the fields
    writer.writerow(fields)
    for row in rows:
        writer.writerow(row)

df = pd.read_csv(filename)

values = {'Product Name': 'Not listed', 'New Price': 0,'Old Price': 0, 'Rating': 'Not Rated'}

rest(2)
print('Filtering data for relevant infomation [...]')
df = df.dropna(thresh=2)
df = df.fillna(value=values)

print('Analytics: ')
print(str(df.count()))


df.to_csv(filename)

print("Time Duration: " + str(round(time.time() - start_time, 2)) + 'secs')


