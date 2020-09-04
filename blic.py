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

    
    # if len(old_titles) > 0:
    #     #add new titles
    #       with open(file_name, 'a', 
    #               encoding = 'utf-8') as f:
    #             for news in all_news:
    #                 title = news.title.getText().strip()
    #                 link = news.guid.getText()
                    
    #                 if not title in old_titles:
    #                     f.write(f'{title}, {link}\n')
    #                     print('added title: ', title)
    #                     old_titles.add(title)
                    
    # else:
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding='utf-8') as f:
    #           for news in all_news:
    #             title = news.title.getText()
    #             link = news.guid.getText()
               
    #             f.write(f'{title}, {link}\n')
    
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