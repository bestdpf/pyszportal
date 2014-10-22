import urllib
import urllib2
import hashlib

url = 'http://219.223.254.66/cgi-bin/srun_portal'

ori_name = ''
ori_pass = ''
val = {'username' : ori_name,
'password' : ori_pass,
'ac_id' : '1',
'type' : '1',
'as_init_port' : '1',
'action' : 'login'
}
data = urllib.urlencode(val)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
