import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from IPython.display import display


url = 'https://www.akchabar.kg/ru/exchange-rates/'
pages = requests.get(url)
soup = BeautifulSoup(pages.text, 'html.parser')
spreadsheet = soup.find('table', id='rates_table')

table = spreadsheet.find_all('span', class_='dib')
table = [item.text for item in table]

header = []

for i in table:
    header.append(i)
    header.append(i)

header.insert(0, ' ')
mydata = pd.DataFrame(columns=header)
date = datetime.now()


for d in spreadsheet.find_all('tr')[1:]:
    row_data = d.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

mydata.to_csv(f'updated_datas_{date}.csv', index=False)
mydata2 = pd.read_csv(f'updated_datas_{date}.csv')
display(mydata2.to_string())

