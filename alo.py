# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:54:20 2020

@author: Nikola
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
    
    url = 'https://www.alo.rs'
    
    alo = reqs.get(url)
    alo.raise_for_status()
    
    page = BeautifulSoup(alo.text, 'html.parser')
       
    all_news = page.findAll('h2')
    all_news.extend(page.findAll('h3'))
    all_news.extend(page.findAll('h4'))
    # if len(old_titles) > 0:
    #     #add new titles
    #       with open(file_name, 'a', 
    #               encoding = 'utf-8') as f:
    #             for news in all_news:
                   
    #                 title = news.getText().strip()
    #                 new_line = title.find('\n')
    #                 first_char = new_line + 1
    #                 while not str.isalpha(title[first_char]):
    #                     first_char+=1
                     
    #                 title = title[0:new_line] + ' ' + title[first_char:]
                    
    #                 #skipping 'sport' , 'vip ', etc..
    #                 if len(title) < 25:
    #                     continue
                    
    #                 try:
    #                     link = url + news.a['href']
    #                     if not title in old_titles:
    #                         f.write(f'{title}, {link}\n')
    #                         print('added title: ', title)
    #                         old_titles.add(title)
                    
    #                 except:
    #                     #no links in h2/h3/h4
    #                     pass
                   
                    
    # else:
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding='utf-8') as f:
    #           for news in all_news:
                 
    #              #TODO better clearing of spaces...
    #              title = news.getText().strip()
    #              new_line = title.find('\n')
    #              first_char = new_line + 1
    #              while not str.isalpha(title[first_char]):
    #                  first_char+=1
                     
    #              title = title[0:new_line] + ' ' + title[first_char:]
                 
    #               #skipping 'sport' , 'vip ', etc..
    #              if len(title) < 25:
    #                   continue
                    
                 
    #              try:
    #                  link = url + news.a['href']
    #                  f.write(f'{title}, {link}\n')
    #              except:
    #                  #no links in h2/h3/h4
    #                  pass

    res = dict()
    
    for news in all_news:
        title = news.getText().strip()
        new_line = title.find('\n')
        first_char = new_line + 1
        while not str.isalpha(title[first_char]):
            first_char+=1
         
        title = title[0:new_line] + ' ' + title[first_char:]
        
        #skipping 'sport' , 'vip ', etc..
        if len(title) < 25:
            continue
        
        try:
            link = url + news.a['href']
            res[title] = link
            
        except:
            #no links in h2/h3/h4
            pass
        
    
    return res
                 
if __name__ == '__main__':
    news = main()
    
    for k,v in news.items():
        print(v)
                 
                 