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
    
    
    # if len(old_titles) > 0:
    #     #add new titles
    #      with open(file_name, 'a', 
    #               encoding = 'utf-8') as f:
    #            for news in all_news:
    #                 link = news.a['href']
    #                 if link.find('www') == -1:
    #                     link = kurir + link
    #                 title = news.find('h2').getText().strip()
    #                 if title.find('\n') != -1:
    #                     title = title[:title.find('\n')].strip()
                        
    #                 if not title in old_titles:
    #                     f.write(f'{title}, {link}\n')
    #                     print('added title: ', title)
    #                     old_titles.add(title)
                    
    # else:
    #     print('adding all titles...')
    #     with open(file_name, 'w', encoding='utf-8') as f:
    #           for news in all_news:
    #             link = news.a['href']
    #             if link.find('www') == -1:
    #                 link = kurir + link
    #             title = news.find('h2').getText().strip()
    #             if title.find('\n') != -1:
    #                 title = title[:title.find('\n')].strip()
    #             f.write(f'{title}, {link}\n')
    
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