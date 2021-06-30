# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:25:53 2020

@author: Nikola
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
    
    kurir = 'https://www.kurir.rs'
    
    page = reqs.get(kurir)
    page.raise_for_status()
    
    soup = BeautifulSoup(page.text, 'html.parser')
    
    all_news = soup.findAll('div',  {'class' : 'itemContent'})
    
    res = dict()
    
    for news in all_news:
        link = news.a['href']
        if link.find('www') == -1:
            link = kurir + link
        title = news.find('h2').getText().strip()
        if title.find('\n') != -1:
            title = title[:title.find('\n')].strip()
        
        res[title] = link
    
    return res
                
if __name__ == '__main__':
    news = main()
    for k,v in news.items():
        print(v)