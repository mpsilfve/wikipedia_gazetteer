# Wikipedia Gazetteer

Named entity gazetteer derived from the Finnish Wikipedia.

# General Stuff

This code will build a gazetteer or Finnish Named Entity Recognition from the Finnish Wikipedia. A gazetteer maps terms into categories. For example, the gazetteer built by this code maps "Samsung" into the category "Yritys" (Finnish for company) and "Nokia" into the categories "Yritys" and "Suomen kunta" (Finnish town). 

Categories are based on Wikipedia infoboxes. Some articles lack an infobox (e.g. the article for ThinkPad in the Finnish Wikipedia). Terms corresponding to these articles do not currently receive any categories.

This project relies on an xml-dump of the Finnish Wikipedia. You can get one e.g. from the [DBPedia project] (http://downloads.dbpedia.org/2015-10/core-i18n/fi/pages_articles_fi.xml.bz2).

You can possibly also use the code to generate gazetteers for other languages but I have't tested this. 

# Building

Run

    make
    
This will build a Python3 pickled dictionary ```fi_wikipedia_gazetteer.pkl```.

# Using

    $ python3
    >>> import pickle
    >>> gazetteer = pickle.load(open('fi_wikipedia_gazetteer.pkl','rb'))
    >>> gazetteer['Nokia']
    {'Yritys', 'Suomen kunta'}
    >>> gazetteer['Samsung']
    {'Yritys'}

# Releases

Look in releases for the latest compiled version if you don't want to compile the gazetteer yourself.
