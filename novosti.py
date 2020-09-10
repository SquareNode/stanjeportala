# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:30:12 2020

@author: Nikola

scaping novosti rss feed, contains only todays news
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
    
    url = 'https://www.novosti.rs/rss/danasnje-vesti'
    
    novosti = reqs.get(url)
    novosti.raise_for_status()
    
    page = BeautifulSoup(novosti.text, 'xml')
    
    all_news = page.findAll('item')
        
    res = dict()
    
    for news in all_news:
        title = news.title.getText()
        link = news.link.getText()
        res[title] = link
    return res
    
if __name__ == '__main__':
    news= main()
    for k,v in news.items():
        print(v)