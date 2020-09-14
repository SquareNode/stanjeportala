# -*- coding: utf-8 -*-
"""
Created on Fri Sep	4 11:11:45 2020

@author: Nikola

calling all main functions of modules, they return dicts
taking those dicts in {title : link} format and writing to DB
along with the date
checking for duplicates while doing it
"""

	
import kurir, alo, n1, srbijadanas, telegraf, espreso, b92, blic, danas
import informer, novosti, pymongo, datetime, os
from pymongo import MongoClient
from dotenv import load_dotenv

def do_work(db, col_name, scraped_news):
	
	print(col_name)
	col = db[col_name]
	db_news = col.find()
	
	n = 0
	
	db_titles = [news['title'] for news in db_news]
	
	date_str = str(datetime.datetime.now().date())
	
	for title,link in scraped_news.items():
		if not title in db_titles:
			col.insert_one({'title': title, 'link' : link, 'date' : date_str})
			n+=1
			
	print(f'inserted {n} news')


if __name__ == '__main__':
	
	try:
		env_path = os.path.join(os.path.dirname(__file__), '.env')
		load_dotenv(env_path)
	#no .env on heroku, our env vars are already available
	except:
		pass
		
	
	cluster = MongoClient(f'mongodb+srv://{os.environ.get("DB_USERNAME")}'
	+ f':{os.environ.get("DB_PASSWORD")}@cluster0.udsmc.mongodb.net'
	+ f'/{os.environ.get("DB_NAME")}?retryWrites=true&w=majority')
	
	db = cluster['test']
	col = db['topnews']
		
	news_dict = kurir.main()
	do_work(db, 'kurir', news_dict)
	
	news_dict = alo.main()
	do_work(db, 'alo', news_dict)
	
	news_dict = n1.main()
	do_work(db, 'n1', news_dict)
	
	news_dict = danas.main()
	do_work(db, 'danas', news_dict)
	
	news_dict = srbijadanas.main()
	do_work(db, 'srbijadanas', news_dict)
	
	news_dict = blic.main()
	do_work(db, 'blic', news_dict)
	
	news_dict = espreso.main()
	do_work(db, 'espreso', news_dict)
	
	news_dict = telegraf.main()
	do_work(db, 'telegraf', news_dict)
	
	news_dict = b92.main()
	do_work(db, 'b92', news_dict)
	
	news_dict = informer.main()
	do_work(db, 'informer', news_dict)
	
	news_dict = novosti.main()
	do_work(db, 'novosti', news_dict)
	