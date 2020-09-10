# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:59:00 2020

@author: Nikola

scraping informer rss feed
rss feed contains only news published today
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
    
    url = 'https://informer.rs/rss/danasnje-vesti'
    
    informer = reqs.get(url)
    informer.raise_for_status()
    
    page = BeautifulSoup(informer.text, 'xml')
    
    all_news = page.findAll('item')
    
    res = dict()
    for news in all_news:
        title = news.title.getText()
        link = news.link.getText()
        res[title] = link
    
    return res
                    
if __name__ == '__main__':
    news = main()
    
    for k,v in news.items():
        print(v)