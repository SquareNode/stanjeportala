# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:12:29 2020

@author: Nikola

scraping the rss feed of srbijadanas, checking the dates
"""


import sys, requests as reqs, datetime
from bs4 import BeautifulSoup

def check_date(news):
	
	str_date = news.pubDate.getText()
	#Ponedeljak, August 31, 2020 - 13:01
	tokens = str_date.split()
	month = datetime.datetime.strptime(tokens[1][:3], '%b').month
	day = int(tokens[2][:-1])
	yr = int(tokens[3])

	return datetime.date.today() == datetime.date(yr, month, day)


def main():
	
	url = 'https://www.srbijadanas.com/rss.xml'
	
	srbijadanas = reqs.get(url)
	srbijadanas.raise_for_status()
	
	page = BeautifulSoup(srbijadanas.text, 'xml')
	
	all_news = page.findAll('item')

	res = dict()
	
	for news in all_news:
		if check_date(news):
			title = news.title.getText()
			link = news.link.getText()
			res[title] = link
	
	return res
	
if __name__ == '__main__':
	news = main()
	for k,v in news.items():
		print(v)
