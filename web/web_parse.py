import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url_template = input('Enter url: ')
file_name = input('Enter output file name: ')

def parse(url = url_template):
    result_list = {'link': [], 'title': []}
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    links = soup.find_all('h3', class_='Mb(5px)')
    for i in links:
        result_list['link'].append('finance.yahoo.com'+i.a['href'])
        result_list['title'].append(i.contents[0].text)
    return result_list

df = pd.DataFrame(data=parse())
df.to_csv(file_name, index=False)