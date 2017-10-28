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
        
        site = mwclient.Site((protocol, host))
        
        if user and pwd :
                # Login parameters
                site.login(user, pwd)
                        
        
        # Example actions ahead
        
        # Retrieve content from article
        # Notice unicode stuff
        page = site.pages[u'Universitat Autònoma de Barcelona']
        
        if page.exists :
                # Notice if priting in utf8
                # https://www.mediawiki.org/wiki/API:Main_page -> Retrieve text
                print( page.text().encode('utf8') )
                
                # Get all links https://www.mediawiki.org/wiki/API:Links
                # Page object information https://github.com/mwclient/mwclient/blob/master/mwclient/page.py
                
                links = page.links()
                for link in links :
                        print( link.name.encode('utf8') )
                
                # Get all images https://www.mediawiki.org/wiki/API:Images
                images = page.images()
                for image in images :
                        print( image.name.encode('utf8') )
                                
                # Get all images https://www.mediawiki.org/wiki/API:Images
                images = page.images()
                for image in images :
                        print( image.name.encode('utf8') )

                # Get all revisions https://www.mediawiki.org/wiki/API:Main_page
                revisions = page.revisions()
                for revision in revisions :
                        dt = datetime.datetime.fromtimestamp( time.mktime( revision['timestamp'] ) )
                        revtime = '{}'.format(dt.strftime('%F %T'))
                        print( revision['user'].encode('utf8') + " on ".encode('utf8') + revtime.encode('utf8') )



                # Retrieve pageviews
                result = site.api('query', prop='pageviews', titles=u'Bellaterra|Cerdanyola del Vallès')
                
                for page in result['query']['pages'].values():
                        if 'pageviews' in page:
                                print( '{}'.format(page['title'].encode('utf8') ) )
                                pp.pprint( page['pageviews'] )
                
                                # Solve this case....


if __name__ == "__main__":
	main(sys.argv[1:])
