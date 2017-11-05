#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import os.path
import json
import wikidata.client
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas
import argparse
import time
import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

def main(argv):



        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        
        query = """SELECT ?uni ?uniLabel ?date WHERE {
        ?uni wdt:P31 wd:Q875538 .
        ?uni wdt:P571 ?date .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "ca" . }
        }
        limit 10
        """
        
        sparql.setQuery( query )
        
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        results_df = pandas.io.json.json_normalize(results['results']['bindings'])

        # Noticice, this below is just for sake of combining 2 tools. We could get this straight from SPARQL
        client = wikidata.client.Client()
        web_url = client.get('P856')
        
        for index, row in results_df.iterrows():
                        # pp.pprint( row ) Careful unicode
                        urlvalue = row['uni.value']
                        value = urlvalue.replace( "http://www.wikidata.org/entity/", "" )
                        print( value )
                        # URL of the website
                        entity = client.get(value, load=True)
                        url = entity[ web_url ]
                        print( url )


if __name__ == "__main__":
        main(sys.argv[1:])
