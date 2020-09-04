# -*- coding: utf-8 -*-
"""
Created on Tue Sep	1 12:54:10 2020

@author: Nikola
"""


import sys, requests as reqs, datetime
from bs4 import BeautifulSoup
from tools import get_titles


def main():
	
	
	url = 'https://www.telegraf.rs/'
	
	telegraf = reqs.get(url)
	telegraf.raise_for_status()
	
	page = BeautifulSoup(telegraf.text, 'html.parser')
	
	all_news = page.findAll('div', {'class' : 'grid-image-wrapper'})
	
	# if len(old_titles) > 0:
		
		# with open(file_name, 'a', encoding = 'utf-8') as f:
			# for news in all_news:
				# title = news.a['title']
				# link = news.a['href']
				# if not title in old_titles:
					# f.write(f'{title}, {link}\n')
					# old_titles.add(title)
					# print('added title', title)
	# else:
		# print('adding all titles...')
		# with open(file_name, 'w', encoding='utf-8') as f:
			# for news in all_news:
				# title = news.a['title']
				# link = news.a['href']
				# f.write(f'{title}, {link}\n')
	
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
			
				