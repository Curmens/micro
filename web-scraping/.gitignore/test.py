from bs4 import BeautifulSoup as bs
import requests, re, itertools, time


# base_url = 'https://www.tonaton.com.gh'
# # url = base_url + f'/computing/?q=mouse&page=1'
# r = requests.get(base_url)
# data = r.text
# webpage = bs(data)

stride = '<div class = "sample" > GH¢ 3 900. < /div >'

check = re.findall(r'\d+', stride)
print(''.join(check))

# url = webpage.find('a', attrs={"aria-label": "Next Page"})["href"]
# print(url)

# last = webpage.findAll('a', attrs={'aria-label': 'Last Page'})
# print(last)

# pattern = r'page=([\d]+)'

# max_page = int(re.search(pattern, str(last)).group(1))
# print(max_page)
# print(type(max_page))

# print(webpage)
