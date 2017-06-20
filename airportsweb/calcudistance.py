# -*- coding: utf-8 -*- 

class airport_list_name (object):

    def __init__(self, fn='data\gaycone.json'):
       import json
       with open(fn, 'r', encoding='utf8') as infile:
           dd = json.load (infile)
