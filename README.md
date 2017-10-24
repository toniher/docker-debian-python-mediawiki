# docker-debian-python-mediawiki
Docker image for python MediaWiki client libraries

Some scripts and configuration options can be found at scripts directory

Building the image:

	docker build -t debian-python-mediawiki .


Executing Docker image (we mount /scripts, accessible then from host)

	docker run -d -v $PWD/scripts:/scripts  --name mwclient debian-python-mediawiki tail -f /dev/null

	docker exec -ti mwclient /bin/bash

Built image does not include example scripts. Retrieve them from the repository via a volume, as pointed above.


* Mwclient Documentation and examples at: http://mwclient.readthedocs.io

