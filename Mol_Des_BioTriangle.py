# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import requests
from bs4 import BeautifulSoup

mySmiles = 'CN1CCC[C@H]1c2cccnc2'
myurl = 'http://biotriangle.scbdd.com/chemical/chemical-text/'
pyload = [('Smiles','CN1CCC[C@H]1c2cccnc2'),   
          ('check_box_2d', 'constitution'),
          ('check_box_2d', 'topology')]



data1 = requests.post(myurl,data = pyload)

soup1 = BeautifulSoup(data1.text,'lxml')

dd = soup1.select('body > div:nth-child(2) > div:nth-child(2) > div > table')
for  row in dd[0].findAll("tr"):
    for colj in row.findAll("td"):
        print(colj.get_text())
print("--------end-------")