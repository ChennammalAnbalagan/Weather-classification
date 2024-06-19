# importing the library
import requests
from bs4 import BeautifulSoup
import xlsxwriter as xl
# enter city name
city =str(input(" Enter the city name: "))
w=xl.Workbook("weather report.xlsx")
w1=w.add_worksheet(city)
# create url
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = str.split('\n')
time = data[0]
sky = data[1]
# list having all div tags having particular class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]
# printing all the data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
w1.write(0,0,'Temperature')
w1.write(0,1,'Time')
w1.write(0,2,'Sky')
w1.write(0,3,'Other data')
w1.write(1,0,temp)
w1.write(1,1,time)
w1.write(1,2,sky)
w1.write(1,3,other_data)
w.close()