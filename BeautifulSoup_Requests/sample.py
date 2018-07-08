
import requests
from bs4 import BeautifulSoup
# =============================================================================
# l=[]
# p={}
# 
# =============================================================================

# =============================================================================
# source=requests.get('https://internshala.com/internships/machine%20learning-internship-in-bangalore').text
# soup=BeautifulSoup(source,'lxml')
# for c in (soup.find('div',attrs={"id":"content"})).findAll('div',attrs={"class":"individual_internship_header"}):
#    d=c.find('div')
#     l.append((d.h4.a)['href'])
# t=c.find('div',attrs={"class":"individual_internship_header"})
# 
# =============================================================================
# =============================================================================
# source1=requests.get('https://internshala.com/internship/detail/nlp-machine-learning-internship-in-bangalore-at-primenumbers-technologies1528394254').text
# soup1=BeautifulSoup(source1,'lxml')
# main=soup1.find('div',attrs={"class":"table-row"})
# internship_meta=main.find('div',attrs={"class":"internship_meta"})
# internship=internship_meta.h4.text
# company=internship_meta.a.text
# location=internship_meta.p.a.text
# 
# table=(internship_meta.find('thead')).findAll('th')
# table1=(internship_meta.find('tbody')).findAll('td')
# table[:]=map(lambda x: x.text, table)
# table1[:]=map(lambda x: x.text, table1)
# p=dict(zip(table,table1))
# 
# =============================================================================
