# -*- coding: utf-8 -*-
"""
Created on Tue Sep	1 12:54:10 2020

@author: Nikola
"""


import sys, requests as reqs, datetime
from bs4 import BeautifulSoup

def main():
	
	
	url = 'https://www.telegraf.rs/'
	
	telegraf = reqs.get(url)
	telegraf.raise_for_status()
	
	page = BeautifulSoup(telegraf.text, 'html.parser')
	
	all_news = page.findAll('div', {'class' : 'grid-image-wrapper'})
	
	res = dict()
	
	for news in all_news:
		title = news.a['title']
		link = news.a['href']
		res[title] = link
		
	return res
				
if __name__ == '__main__':
	news = main()				 
	
	for k,v in news.items():
		print(v)