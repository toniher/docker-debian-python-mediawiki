#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import os.path
import json
import mwclient
import wikidata.client
import argparse
import time
import datetime
import pprint

parser = argparse.ArgumentParser(description="""Script for testing MediaWiki API""")
parser.add_argument("-config",help="""Path to a JSON file with configuration options!""")
parser.add_argument("-search", help="""Search String""")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

def main(argv):
        
        
        host = "localhost"
        user = None
        password = None
        protocol = "http"
        lang = "ca"
        data = {}
        # Search string
        searchStr = u"Universitat Autònoma de Barcelona"
        
        if "config" in args:
                with open(args.config) as json_data_file:
                                data = json.load(json_data_file)
        
        if args.search is not None:
                searchStr = args.search
        
        if "mw" in data:
                if "host" in data["mw"]:
                        host = data["mw"]["host"]
                if "user" in data["mw"]:
                        user = data["mw"]["user"]
                if "password" in data["mw"]:
                        pwd = data["mw"]["password"]
                if "protocol" in data["mw"]:
                        protocol = data["mw"]["protocol"]
                if "lang" in data["mw"]:
                        lang = data["mw"]["lang"]
                        
        

        
        # Connect wikidata
        site = mwclient.Site((protocol, host))

        
        # Full text search
        # https://www.mediawiki.org/wiki/API:Search

        # https://www.wikidata.org/w/api.php?action=query&list=search&srsearch=Universitat_Autònoma_de_Barcelona&utf8=
        searchResult = site.search( searchStr )
        for result in searchResult:
                # pp.pprint( result ) Careful printing Unicode
                print("-"+result.get('title'))
        
        querywb = {}
        querywb["search"] = searchStr
        querywb["language"] = lang
        querywb["limit"] = 5
        
        
        # Wikidata client
        client = wikidata.client.Client()

        # Prop instance
        instance_prop = client.get('P31')

        
        # https://www.wikidata.org/w/api.php?action=wbsearchentities&search=Universitat_Autònoma_de_Barcelona&language=ca&limit=5&format=json";
        wbSearchResult = site.api( 'wbsearchentities', "GET", **querywb )
        if 'search' in wbSearchResult:
                for result in wbSearchResult["search"]:
                        #pp.pprint( result )
                        print( "*"+result.get('id'))
                        entity = client.get( result.get('id'), load=True)
                        print( ( str( entity.label ) ).encode('utf-8') )
                        print( entity.description )
                        if instance_prop in entity:
                                instance = entity[ instance_prop ]
                                print( instance.label )
                                


if __name__ == "__main__":
        main(sys.argv[1:])
