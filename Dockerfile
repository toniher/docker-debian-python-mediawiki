FROM biocorecrg/debian-perlbrew-pyenv3:buster

VOLUME /scripts

RUN pip install mwclient==0.10.0 
RUN pip install wikidata==0.6.1
RUN pip install SPARQLWrapper==1.8.4 
RUN pip install pandas==0.25.1

# Adding Jupyter
RUN pip install jupyter

# Locales, for printing
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Clean cache
RUN apt-get clean
RUN set -x; rm -rf /var/lib/apt/lists/*

VOLUME /notebooks

EXPOSE 8888


