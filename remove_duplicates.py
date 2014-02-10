import csv
import sys
import StringIO

from urlparse import urlparse

urls = set()

reader = csv.reader(StringIO.StringIO(sys.stdin.read()))
next(reader, None)
writer = csv.writer(sys.stdout)
writer.writerow(['Title', 'URL', 'Original URL'])
for row in reader:
    try:
        title = row[0]
        url = row[2]
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        netloc = parsed_uri.netloc
        if netloc not in urls:
            urls.add(netloc)
            writer.writerow([title, domain, url])
    except Exception, e:
        continue


