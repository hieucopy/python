import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import csv



filename= open('data.csv', mode ='w')







url ='https://www.formula1.com/en/results.html/2024/drivers.html'
response= requests.get(url)

if response.status_code==200:
    soup =BeautifulSoup(response.content,'html.parser')
#   print(soup.title.text)
    table =soup.find('table', class_="resultsarchive-table")
    
    rows= soup.find_all('tr')
    print(rows)
    for row_id, row in enumerate(rows):
        columns =row. find_all('td')
        print(columns)
        #print(f'row={row_id}:{columns}')
        if columns:
            position= columns[1].text.strip()
            driver_name= columns[2].text.strip().split('\n')
            driver_name= ' '.join(driver_name[:-1])
            nationality=columns[3].text.strip()
            car =columns[4].text.strip()
            pts =columns[5].text.strip()
            roww=[position,driver_name,nationality,car,pts]
            roww=','.join(roww)
            roww=roww+'\n'
            filename.write(roww)
          
filename.close()