Normalize a CSV containing a link title and url. 

Turns:
Title,URL
My Awesome Website,http://example.com/what/ever/this/is
A Duplicate Website,http://example.com/who/is/that

Into:
Title,URL,Original URL
My Awesome Website,http://example.com,http://example.com/what/ever/this/is


Usage: 
python concat.py first.csv second.csv | python base_urls.py | python remove_duplicates.py > final.csv


