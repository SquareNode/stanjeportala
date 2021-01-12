# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:29:46 2020

@author: Nikola

scraping n1 xml feed
"""


import sys, requests as reqs
from bs4 import BeautifulSoup
	
def main():
	
	url = 'https://rs.n1info.com/feed/'
	n1 = reqs.get(url)
	n1.raise_for_status()
	
	page = BeautifulSoup(n1.text, 'xml')
	
	all_news = page.findAll('item')
	
	res = dict()
	
	for news in all_news:
		link = news.link.getText()
		title = news.title.getText()
		if link.find('english') == -1:
			res[title] = link
	
	return res
			
	
	
if __name__ == '__main__':
	n = main()
	
	with open('test.txt', 'w', encoding='utf-8') as f:
		
		for k,v in n.items():

			f.write(f'{k}, {v}\n')
