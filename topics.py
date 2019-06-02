import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url = 'https://www.giveindia.org/certified-indian-ngos'
def getRequestSoup(url):
	return BeautifulSoup(requests.get(url).text,'html.parser')
first_call = getRequestSoup(url)
# print (first_call)
def list_of_ngo(url):
    dic = {}
    soup = url.find('div', class_="ngo-list-desktop display-desktop-only col-12 col-sm-12 col-md-12 col-lg-12")
    table = soup.find('table', class_="jsx-697282504 certified-ngo-table")
    tr = table.find_all('tr', class_="jsx-697282504")
    one_list = []
    two_list = []
    three_list = []
    for i in tr:
        td = i.find_all('td', class_="jsx-697282504")
        for one in td[:1]:
            text_1 = one.text
            one_list.append(text_1)
           
        for two in td[1:2]:
            text_2 = two.text
            two_list.append(text_2)
           
        for three in td[2:3]:
            text_3 = three.text
            three_list.append(text_3)
        dic['state'] = three_list
        dic['name'] = one_list
        dic['cause'] = two_list
    return dic
ngos_list =list_of_ngo(first_call)
pprint (ngos_list)

def state_by_ngo(list1):
    dic = {}
    for (a, b, c) in zip(list1['name'], list1['cause'], list1['state']): 
        if c in dic:
            dic[c].append(a)
        else:
            dic[c] = [a]
        # with open('/home/rupa/Documents/saral_data_scraper/ngo_state/'+ c +'.json', 'w') as f:
        #     json.dump(dic, f, indent=1)    
    return dic        
pprint (state_by_ngo(ngos_list))



#












































































# # print (first_call)
# def first(url):
#     soup = url.find('div', class_="mw-content-ltr")
#     t = soup.find('div', class_="mw-parser-output")
#     s = t.find('table', class_='wikitable sortable')
#     l = []
#     dic= {}
#     for a in s.find_all('th'):
#         ttags = a.text
#         p = ttags.split()
#         l.extend(p)
#     key  = l[1]
#     tb = s.find('tbody')
#     for i in tb.find_all('td'):
#         print (i.text)
#         # for j in i.find_all('a'):
#         #     a = j.text
#         #     dic[key] = a
#         #     print (dic)
# first(first_call)  






































# def first(url1):
#     div = url1.find('div', class_="w3-bar-block")
#     for i in div.find_all('div', class_="w3-container"):
#         # print(i.text)
#         for a in div.find_all('a'):
#             atags = a.text
#             print (atags) 
#             # dic = {}    
#             # dic[i.text] = atags 
#             # print (dic)   
#             urls = 'https://www.w3schools.com'+ a.get('href') 
#             data = getRequestSoup(urls)    
#             # print (data)
#             soup = data.find('div', class_="w3-light-grey")
#             # print (soup)
#             for a in soup.find_all('a'):
#                 print (a.text)
              
# second_call = first(first_call)        
