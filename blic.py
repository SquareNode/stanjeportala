# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:30:16 2020

@author: Nikola
"""


import sys, requests as reqs
from bs4 import BeautifulSoup


def main():   
    
    blic = 'https://www.blic.rs/rss/danasnje-vesti'
    
    page = reqs.get(blic)
    page.raise_for_status()
    
    soup = BeautifulSoup(page.text, 'xml')
    
    all_news = soup.findAll('item')

    res = dict()
    
    for news in all_news:
        title = news.title.getText().strip()
        link = news.guid.getText()
        res[title] = link    
    
    return res
            
if __name__ == '__main__':
    news = main()
    
    for k,v in news.items():
        print(k,v)