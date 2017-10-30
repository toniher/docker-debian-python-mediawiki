#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import os.path
import json
import mwclient
from wikidata.client import Client
import argparse
import time
import datetime
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
		
		if "config" in args:
				with open(args.config) as json_data_file:
						data = json.load(json_data_file)
		
		if "mw" in data:
				if "host" in data["mw"]:
						host = data["mw"]["host"]
				if "user" in data["mw"]:
						user = data["mw"]["user"]
				if "password" in data["mw"]:
						pwd = data["mw"]["password"]
				if "protocol" in data["mw"]:
						protocol = data["mw"]["protocol"]


		client = Client()
		entity = client.get('Q20145', load=True)
		pp.pprint( entity )
	
if __name__ == "__main__":
	main(sys.argv[1:])
