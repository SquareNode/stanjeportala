# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:29:46 2020

@author: Nikola

scraping n1, latest news page
taking only today's ones
"""


import sys, requests as reqs
from bs4 import BeautifulSoup

def check_date(date_string):
	"""
	date_string : 09:23 h or 31.08.2020.
	today's news get hour stamp, other get date stamp
	"""
	if date_string.find('h') > 0:
		return True
	return False

def main():
	
	url = 'http://rs.n1info.com/Najnovije'
	
	n1 = reqs.get(url)
	n1.raise_for_status()
	
	page = BeautifulSoup(n1.text, 'html.parser')
	
	all_news = page.find('div', {'class' : 'news-content-list'})
	all_news = all_news.findAll('h2', {'class' : 'title'})
	
	res = dict()
	
	for news in all_news:
		link = news.a['href']
		title = news.a.getText()
		if check_date(news.span.getText()):
			res[title] = link
			
	return res
	
	
if __name__ == '__main__':
	n = main()					 
	
	with open('test.txt', 'w', encoding='utf-8') as f:
		
		for k,v in n.items():

			f.write(f'{k}, {v}\n')
