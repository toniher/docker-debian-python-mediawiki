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
        """
        
        sparql.setQuery( query )
        
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        results_df = pandas.io.json.json_normalize(results['results']['bindings'])
        
        for index, row in results_df.iterrows():
                        pp.pprint( row )
                        #urlvalue = row['item.value']
                        #value = urlvalue.replace( "http://www.wikidata.org/entity/", "" )
                        #print( value )

           


        # client = wikidata.client.Client()
        # entity = client.get('Q20145', load=True)
        # pp.pprint( entity )

if __name__ == "__main__":
        main(sys.argv[1:])
