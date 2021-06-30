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
	
	res = dict()
	
	for news in all_news:
		title = news.getText().strip()
		if len(title) < 8:
			continue
		try:
			link = news.a['href']
			#skipping alo.rs and prva.rs news
			skipping = ['alo.rs', 'prva.rs']
			to_skip = False
			for s in skipping:
				if link.find(s) != -1:
					to_skip = True
			
			if to_skip:
				continue
			#adding base link to slash style links
			if link.find('b92.net') == -1:
				link = url + link
			
			res[title] = link
		except:
			pass
	
	return res


if __name__ == '__main__':
	news = main()
	
	with open('test.txt', 'w', encoding = 'utf-8') as f:
		for k,v in news.items():
			f.write(f'{k}, {v}\n')