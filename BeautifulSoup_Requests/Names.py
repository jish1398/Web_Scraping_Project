# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:02:44 2018

@author: jishn
"""
import requests
from bs4 import BeautifulSoup

list={}
source2=requests.get('https://internshala.com/internships/').text
soup2=BeautifulSoup(source2,'lxml')
category=(soup2.find('div',attrs={"id":"content"})).find('select',attrs={"id":"select_category"})
print(category)

# =============================================================================
# category_list=category.findAll('option')
# for i in category_list:
#     list[i.text]=i['value']
# =============================================================================
