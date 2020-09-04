# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:32:21 2020

@author: Nikola
"""


import sys, requests as reqs
from bs4 import BeautifulSoup


def main():
        
    url = 'https://www.b92.net'
    
    b92 = reqs.get(url)
    b92.raise_for_status()
    
    page = BeautifulSoup(b92.text, 'html.parser')
    
    all_news = page.findAll('h2')
    all_news.extend(page.findAll('h3'))
    all_news.extend(page.findAll('h4'))
    
        
    # if len(old_titles) > 0:
    #     #add all titles
    #     with open(file_name, 'a', 
    #               encoding = 'utf-8') as f:
    #         for news in all_news:
                    
    #             title = news.getText().strip()
                
    #             if len(title) < 8:
    #                 continue
                
    #             try:
    #                 link = url + news.a['href']
    #                 if not title in old_titles:
    #                      f.write(f'{title}, {link}\n')
    #                      print('added title: ', title)
    #                      old_titles.add(title)
                
    #             except:
    #                 #no link in title
    #                 pass
    
    # else:
    #     #add all titles
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding='utf-8') as f:
    #           for news in all_news:
                  
    #               title = news.getText().strip()
                  
    #               if len(title) < 8: 
    #                   continue
                
    #               try:
    #                   link = url + news.a['href']
    #                   f.write(f'{title}, {link}\n')
    #               except:
    #                   #no link
    #                   pass

    
    res = dict()
    
    for news in all_news:
        title = news.getText().strip()
        if len(title) < 8:
            continue
        try:
            link = url + news.a['href']
            res[title] = link
        except:
            pass
    
    
    return res


if __name__ == '__main__':
    news = main()
    
    for k,v in news.items():
        print(v)