from bs4 import BeautifulSoup
import requests
import pymysql
import re

base_url = 'https://www.v2ex.com/?tab=hot'
v2ex_url = 'https://www.v2ex.com/t/'

db = pymysql.connect("localhost", "root", "root", "python")
cursor = db.cursor()

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
a_list = soup.find_all("a", class_="topic-link")
# box = soup.find_all("a", class_="topic-link", href=re.compile("/\d+"))
for a in a_list:
    # print(a)
    pattern = re.compile(r'\d+')
    numList = pattern.findall(a['href'])
    # print(m[0])
    id = numList[0]
    hot = numList[1]
    url = v2ex_url + id
    sql = "insert into v2ex(id, title, url, hot) VALUES('%s', '%s', '%s','%s')" \
          " on duplicate key update hot = '%s';" % (id, a.string, url, hot, hot)
    print(sql)
    cursor.execute(sql)
try:
    db.commit()
except:
    db.rollback()
db.close()
