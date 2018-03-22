## Running scripts

From Catalan Wikipedia, it retrieve all text, links, images, and pageviews of a querypage 

* python basic.py -config cawiki.json -page "MediaWiki"

From Wikidata, it performs a Wikidata fulltext search and an ordinary search of a querypage. Label, description and P31 values are provided

* python wdbasic.py -config wd.json -search "Python"

From Wikidata SPARQL endpoint it retrieves a result of a defined SPARQL query and performs an additional property query for each page

* python wdsparql.py

Into a wiki specified in config file, save a text in a page, if OK, add another text and finally uploads a file

* python edit.py -config edit.json -fileup proboscis.jpg


Image proboscis.jpg from: https://commons.wikimedia.org/wiki/File:Proboscis_monkey_(Nasalis_larvatus)_composite.jpg
