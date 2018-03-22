FROM biocorecrg/debian-perlbrew-pyenv3

VOLUME /scripts

RUN pip install mwclient
RUN pip install wikidata
RUN pip install SPARQLWrapper
RUN pip install pandas

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


