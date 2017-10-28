#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import os.path
import json
import mwclient
import argparse
import time
import datetime
import pprint
import logging
logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser(description="""Script for testing MediaWiki API""")
parser.add_argument("-config",help="""Path to a JSON file with configuration options!""")
parser.add_argument("-fileup",help="""File to be uploaded""")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

def main(argv):

	host = "localhost"
	user = None
	password = None
	protocol = "http"
	data = {}
	fileup = None

        
        if 'config' in args:
                with open(args.config) as json_data_file:
                        data = json.load(json_data_file)
        

	if 'fileup' in args:
		fileup = args.fileup

        if "mw" in data:
                if "host" in data["mw"]:
                        host = data["mw"]["host"]
                if "user" in data["mw"]:
                        user = data["mw"]["user"]
                if "password" in data["mw"]:
                        pwd = data["mw"]["password"]
                if "protocol" in data["mw"]:
                        protocol = data["mw"]["protocol"]
        
        site = mwclient.Site((protocol, host))
        
        if user and pwd :
                # Login parameters
                site.login(user, pwd)

        
        page = site.pages[u'Hacking']
        
        if page.can('edit') :

		page.save(u'My first hacking', summary=u'I did it', minor=False, bot=True )

		if page.exists :

			text = page.text()
			more = u'My little pony'

			text = text+more
			page.save( text, summary=u'I did it again', minor=False, bot=True )


	if fileup :
		site.upload(open( fileup ), 'myfile.jpg', 'My image')
		

if __name__ == "__main__":
	main(sys.argv[1:])
