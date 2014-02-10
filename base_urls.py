import csv
import sys
import StringIO

from urlparse import urlparse

input_file = StringIO.StringIO(sys.stdin.read())
reader = csv.reader(input_file)
next(reader, None) # skip headers

writer = csv.writer(sys.stdout)
writer.writerow(["Title", "URL", "Original URL"])
for row in reader:
    try:
        title = row[0]
        url = row[1]
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        writer.writerow([title, domain, url])
    except Exception, e:
        continue
