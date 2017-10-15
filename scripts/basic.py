#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import os.path
import json
import mwclient
import argparse
import time
import pprint

parser = argparse.ArgumentParser(description="""Script for testing MediaWiki API""")
parser.add_argument("-config",help="""Path to a JSON file with configuration options!""")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

def main(argv):
		
		host = "localhost"
		user = None
		password = None
		protocol = "http"
		data = {}
		
		if args.config:
				with open(args.config) as json_data_file:
						data = json.load(json_data_file)
		
		if data.has_key("mw"):
				if data["mw"].has_key("host"):
								host = data["mw"]["host"]
				if data["mw"].has_key("user"):
								user = data["mw"]["user"]
				if data["mw"].has_key("password"):
								pwd = data["mw"]["password"]
				if data["mw"].has_key("protocol"):
								protocol = data["mw"]["protocol"]
		
		site = mwclient.Site((protocol, host))
		
		if user and password :
				# Login parameters
				site.login(user, pwd)
				
		
		# Example actions ahead
		
		# Retrieve content from article
		# Notice unicode stuff
		page = site.pages[u'Universitat Autònoma de Barcelona']
		
		if page.exists :
				# Notice if priting in utf8
				print page.text().encode('utf8')
				
				# Get all links https://www.mediawiki.org/wiki/API:Links
				# Page object information https://github.com/mwclient/mwclient/blob/master/mwclient/page.py
				
				links = page.links()
				for link in links :
						print link.name.encode('utf8')
				
				# Get all images https://www.mediawiki.org/wiki/API:Images
				images = page.images()
				for image in images :
						print image.name.encode('utf8')

if __name__ == "__main__":
		main(sys.argv[1:])
