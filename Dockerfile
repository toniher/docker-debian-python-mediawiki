FROM biocorecrg/debian-perlbrew-pyenv3

VOLUME /scripts

RUN pip install mwclient
RUN pip install wikidata
RUN pip install SPARQLWrapper
RUN pip install pandas

# Adding Jupyter
RUN pip install jupyter

VOLUME /notebooks

EXPOSE 8888


