# docker-debian-python-mediawiki
Docker image for python MediaWiki client libraries

Some scripts and configuration options can be found at scripts directory

Executing Docker image (we mount /scripts, accessible then from host)

	docker run -d -v $PWD/scripts:/scripts  --name mwclient debian-python-mediawiki tail -f /dev/null

	docker exec -ti mwclient /bin/bash


For convenience, we may have a pre-existing MediaWiki, Semantic-MediaWiki powered, installation.

You can find it at: https://github.com/toniher/docker-SemanticMediaWiki

For building and executing it for first time:

    sh smw.sh


* Mwclient Documentation and examples at: http://mwclient.readthedocs.io

Use 
    docker inspect --format '{{ .NetworkSettings.IPAddress }}' containername 

in order to retrieve IP of your container and modify JSON files


