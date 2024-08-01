import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/crypto/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
prices = soup.find_all('td', class_='Va(m) Ta(start) Px(10px) Fz(s)')
nameList = []
for price in prices:
    price_value = price.text.strip()
    nameList.append(price_value)


soup = BeautifulSoup(response.text, "html.parser")
prices = soup.find_all('td', class_='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)')
changePercentList = []
changeList = []
priceList = []

count = 0
for price in prices:
    count += 1
    if count % 3 == 0:
        price_value = price.text.strip()
        changePercentList.append(price_value)
count = 0
for price in prices:
    count += 1
    if (count % 3) - 1 == 0:
        price_value = price.text.strip()
        priceList.append(price_value)
count = 0
for price in prices:
    count += 1
    if (count % 3) - 2 == 0:
        price_value = price.text.strip()
        changeList.append(price_value)

finalList = []

count = 0
for item in nameList:
    finalList.append([nameList[count], priceList[count], changeList[count], changePercentList[count]])
    count += 1

print(["Current Name", "Price", "Change", "Change Percent"])
for item in finalList:
    print(item)


