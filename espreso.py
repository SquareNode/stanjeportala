# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:51:24 2020

@author: Nikola

scraping espresso.rs

all are <a> elements, have different classes though

"""

import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
    url = 'https://www.espreso.rs'
    
    espreso = reqs.get(url)
    espreso.raise_for_status()
    
    page = BeautifulSoup(espreso.text, 'html.parser')
    
    all_news = page.findAll('a', {'class' : 'titleWrap'})
    
    widgets = page.findAll('a', {'class' : 'widgetContent'})
        
    # if len(old_titles) > 0:
        
    #     with open(file_name, 'a', encoding = 'utf-8') as f:
            
    #         for news in all_news:
                
    #             title = news['title']
    #             link = url + news['href']
                
    #             if not title in old_titles:
    #                 f.write(f'{title}, {link}\n')
    #                 old_titles.add(title)
    #                 print('added title: ', title)
            
    #         for widget in widgets:
                
    #             title = widget.h2.getText()
    #             link = widget['href']
    #             if not title in old_titles:
    #                 f.write(f'{title}, {link}\n')
    #                 old_titles.add(title)
    #                 print('added title: ', title)
                    
    # else:
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding = 'utf-8') as f:
    #         for news in all_news:
    #             f.write(f'{news["title"]}, {url + news["href"]}\n')
    #         for widget in widgets:
    #             f.write(f'{widget.h2.getText()}, https:{widget["href"]}\n')
    
    res = dict()
    for news in all_news:
        title = news['title']
        link = url + news['href']
        res[title] = link
    
    for widget in widgets:
        title = widget.h2.getText()
        link = widget['href']
        res[title] = link
    
    return res


if __name__ == '__main__':
    news = main()
    
    for k,v in news.items():
        print(v)
   
