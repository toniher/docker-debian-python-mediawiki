#!/usr/bin/env python

import sys
import os
import os.path
import json
import mwclient
import argparse
import time

parser.add_argument("-config",help="""Path to a JSON file with configuration options!""")

def main(argv):
		
		host = "localhost"
		user = None
		password = None
		protocol = "http"
		
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


if __name__ == "__main__":
		main(sys.argv[1:])
