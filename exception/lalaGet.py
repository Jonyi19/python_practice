# ららぽーとに入っている店舗名を取得するスクリプト
# 名古屋だけ取れず

import requests
import re
from bs4 import BeautifulSoup

# ららぽーとの店舗名とpathをdictに取得
def getStoreName():
    base_url = 'https://mitsui-shopping-park.com/lalaport/'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'lxml')
    dict = {}
    for name in soup.find_all("a",class_="child-menu__link",href=re.compile("/lalaport")):
        dict.setdefault(name.string,name.attrs['href'])
    return dict

# ページの遷移pathをlistに格納
for key,value in getStoreName().items():
    base_url = 'https://mitsui-shopping-park.com/'+ str(value) +'shopguide/'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'lxml')
    list = []
    print("----------"+key+"----------")
    for name in soup.find_all("a", href=re.compile("/?start")):
        if name not in list:
            list.append(name.attrs['href'])

    # ページにある店舗名を取得
    for i in range(len(list)-1):
        target_url = 'https://mitsui-shopping-park.com/'+ str(list[i])
        r = requests.get(target_url)
        soup = BeautifulSoup(r.text, 'lxml')
        for name in soup.find_all("dt", class_='shop-name'):
            print(name.string)
