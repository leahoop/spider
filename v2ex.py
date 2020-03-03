from bs4 import BeautifulSoup
import requests
import pymysql
import re

base_url = 'https://www.v2ex.com/?tab=hot'
v2ex_url = 'https://www.v2ex.com'

db = pymysql.connect("localhost", "root", "root", "python")
cursor = db.cursor()

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
box = soup.find_all("a", class_="topic-link", href=re.compile("/t/\d.*"))
for item in box:
    # print(item)
    print(item['href'])
    print(item.string)
    url = v2ex_url + item['href']
    sql = "insert into v2ex(title, url) VALUES ('%s', '%s');" % (item.string, url)
    # sql = "update zhihu set title = ('%s'),url = ('%s') where id = ('%s');" % (title, url, i)
    cursor.execute(sql)
try:
    db.commit()
except:
    db.rollback()
db.close()
