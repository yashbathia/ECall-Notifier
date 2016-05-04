import requests
from bs4 import BeautifulSoup


resp = requests.get('http://www.nasdaq.com/earnings/earnings-calendar.aspx?date=2016-May-04')
soup = BeautifulSoup(resp.text, 'html.parser')
table = soup.find('table',{'class': 'USMN_EarningsCalendar'})
a_tag = table.find_all('a')
companies = []
for val in a_tag:
    if len(val.contents) == 3:
        companies.append(val.contents[0])

print(companies)

#print(soup.prettify())