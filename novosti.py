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
        
    # if len(old_titles) > 0:
        
    #     with open(file_name, 'a', encoding = 'utf-8') as f:
            
    #         for news in all_news:
                
    #             title = news.title.getText()
    #             link = news.link.getText()
                
    #             if not title in old_titles:
    #                 f.write(f'{title}, {link}\n')
    #                 old_titles.add(title)
    #                 print('added title', title)
                    
    # else:
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding = 'utf-8') as f:
    #         for news in all_news:
    #             f.write(f'{news.title.getText()}, {news.link.getText()}\n')
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
                    