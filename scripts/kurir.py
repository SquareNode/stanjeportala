# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:25:53 2020

@author: Nikola
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def main():
	
	kurir = 'https://www.kurir.rs/rss'
	
	page = reqs.get(kurir)
	page.raise_for_status()
	
	page = BeautifulSoup(page.text, 'xml')
	
	all_news = page.findAll('item')
	
	res = dict()
	
	for news in all_news:
		link = news.link.getText()
		title = news.title.getText()
		
		res[title] = link
	
	return res
				
if __name__ == '__main__':
	news = main()
	for k,v in news.items():
		print(v)