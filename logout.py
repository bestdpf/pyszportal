import urllib
import urllib2
import hashlib

url = 'http://219.223.254.66/cgi-bin/srun_portal'

val = {
'action' : 'logout'
}
data = urllib.urlencode(val)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
