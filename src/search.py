#coding:utf-8
import sys
import time
import urllib
import urllib.request
import requests
from bs4  import BeautifulSoup 
import os

# If we need 500 files, then we need 50 pages in page map
# mymap=['0','1','2','3','4','5','6','7']
# Take only one page to prevent to be put into black list
# page map
mymap=['0']

# access search result page
def baidu_search(key_words,pagenum):             
    url='http://www.baidu.com/s?wd='+key_words+'&pn='+mymap[pagenum]
    html=urllib.request.urlopen(url).read()
    return html

# Send 'get' request to w3c validator
def validate(url):
    validaror_url = "https://validator.w3.org/nu/"
    params = { "doc": url, "out": "json"}
    response = requests.get(validaror_url,params=params)    
    # Use "type:error" to locate errors
    error_key = "\"type\":\"error\""
    # Use "subType:warning" to locate warnings
    warning_key = "\"subType\":\"warning\""
    # .text contains entire content of checking result
    return str(response.text.count(error_key)), str(response.text.count(warning_key))
    
# parse html of result page
def deal_key(key_words):
    # create output file        
    if os.path.exists('data')==False:
        os.mkdir('data')
    filename='data\\'+key_words+'.txt'
    fp=open(filename,'wb')
    if fp:
        pass
    else:
        print('Failed to create output file：'+filename)
        return
    
    # parse html of result page one by one 
    x=0
    while x<=mymap.__len__()-1:
        htmlpage=baidu_search(key_words,x)
        soup=BeautifulSoup(htmlpage, "html.parser")
        # Find result links
        for item in soup.findAll("div", {"class": "result"}):
            a_click = item.find('a')
            if a_click:
                fp.write(a_click.get("href").encode('utf-8'))
                # collect errors and warnings
                err, war = validate(a_click.get("href").encode('utf-8'))
                fp.write(b' errors: %b, warnings: %b' % (bytes(err, 'utf8'),bytes(war, 'utf8')))
            fp.write(b'\r\n')
        x=x+1
        fp.write(b'\r\n')
    fp.close()

# entrance
print('Start:')
# search key word
Keyword = input("Please input keyword for searching: ")
deal_key(Keyword)
print('End！')