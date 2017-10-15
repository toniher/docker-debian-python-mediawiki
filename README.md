# docker-debian-python-mediawiki
Docker image for python MediaWiki client libraries

Some scripts and configuration options can be found at scripts directory

Executing Docker image (we mount /scripts, accessible then from host)

	docker run -d -v $PWD/scripts:/scripts  --name mwclient debian-python-mediawiki tail -f /dev/null

	docker exec -ti mwclient /bin/bash


* Mwclient Documentation and examples at: http://mwclient.readthedocs.io

