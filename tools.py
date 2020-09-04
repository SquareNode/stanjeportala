# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:10:05 2020

@author: Nikola
"""


def get_titles(file_name):
    
    res = set()
    
    #if file is present return all titles
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            
            line = f.readline()
            while line:
                #websites have both http and https
                res.add(line[:line.find(', http')].strip())
                line = f.readline()
            
            return res
    #else return empty set
    except:
        return res