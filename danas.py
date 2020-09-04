# -*- coding: utf-8 -*-
"""
Created on Wed Aug	5 19:44:02 2020

@author: Nikola
"""


import requests as reqs
from bs4 import BeautifulSoup as soup

def main():
	
	url = 'https://www.danas.rs/'
	
	danas_rs = reqs.get(url)
	danas_rs.raise_for_status()
	
	page = soup(danas_rs.text, 'html.parser')

	titles = page.findAll('h3')
	
   
	# if len(my_set) > 0:
		# with open(file_name, 'a', 
				  # encoding = 'utf-8') as f:
			# for title in titles:
				# if title.text not in my_set:
					# f.write(f'{title.text}, {title.a["href"]}\n')
					# print('added title: ', title.text)
					# my_set.add(title.text)
	# else:
		# print('adding all titles...')
		# with open(file_name, 'w', encoding='utf-8') as f:
			# for title in titles:
				# f.write(f'{title.text}, {title.a["href"]}\n')
				
	
	res = dict()
	
	for title in titles:
		res[title.text] = title.a['href'] 
	
	return res

if __name__ == '__main__':
	news=  main()
	
	for k,v in news.items():
		print(v)