import httplib
from HTMLParser import HTMLParser

# Class definition
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data
###################

conn = httplib.HTTPConnection('google.com')
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
print ""
print "------------------------------------------"
print ""
#tree = html.fromstring(data1)
parser = MyHTMLParser()
parser.feed(data1)
