# Test various request types:
#r_dir = ureq.request_url_contents(url_navy_dir)
#r_txt = ureq.request_url_contents(url_navy_txt)
#r_img = ureq.request_url_contents(url_navy_img)
#r_404 = ureq.request_url_contents(url_navy_404)
#  print('  apparent_encoding:    {}'.format(r.apparent_encoding))
#  print('  encoding:         {}'.format(r.encoding))
#  print('  headers:        {}'.format(r.headers))
#  print('  is_permanent_redirect:  {}'.format(r.is_permanent_redirect))
#  print('  is_redirect:      {}'.format(r.is_redirect))
#  print('  json:           {}'.format(r.json))
#  print('  links:          {}'.format(r.links))
#  print('  ok:           {}'.format(r.ok))
#  print('  raise_for_status:     {}'.format(r.raise_for_status))
#  print('  raw:          {}'.format(r.raw))
#  print('  reason:         {}'.format(r.reason))
#  print('  request:        {}'.format(r.request))
#  print('  status_code:      {}'.format(r.status_code))

import requests
#import urllib.request
import re
import datetime

_URL_REQUEST_TIMEOUT_S = 20
date_time_re_patterns = ['\\d{2}-.{3}-\\d{4} \\d{2}:\\d{2}',
          '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}']

date_time_parse_patterns = ['%d-%b-%Y %H:%M', '%Y-%m-%d %H:%M']
_HTML_PCRE_HREF_A = re.compile(r'(?<=\<a href=")(?P<href>.*?)(?=">(?P<txt>.*)</a>)')


def request_url(url, username='', password = '', timeout=1, allow_redirects=True):
  # This seems to (maybe) intrinsically handle the 
  #   bad-URL -> redirect to 'oops' page -> return success issue?
  #   In [13]: b = requests.get('https://www.nrlmry.navy.mil/TC/badaddress')
  #   ---------------------------------------------------------------------------
  #   OSError                   Traceback (most recent call last)
  #   OSError: [Errno 101] Network is unreachable
  #   NewConnectionError            Traceback (most recent call last)
  #   NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7df59cde4e48>: Failed to establish a new connection: [Errno 101] Network is unreachable
  #   MaxRetryError               Traceback (most recent call last)
  #   MaxRetryError: HTTPConnectionPool(host='www.nrlmry.navy.mil', port=80): Max retries exceeded with url: /oops.html (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7df59cde4e48>: Failed to establish a new connection: [Errno 101] Network is unreachable',))
  #   ConnectionError               Traceback (most recent call last)
  #   ConnectionError: HTTPConnectionPool(host='www.nrlmry.navy.mil', port=80): Max retries exceeded with url: /oops.html (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7df59cde4e48>: Failed to establish a new connection: [Errno 101] Network is unreachable',))
  return requests.get(url, auth=(username, password), 
                      timeout=timeout, allow_redirects=allow_redirects)


def request_url_contents(*args, decode=True, **kwargs):
  req     = request_url(*args, **kwargs)
  content = req.content
  if (decode and req.apparent_encoding):
    content = content.decode(req.apparent_encoding)
  return content


def request_url_links(*args, **kwargs):
  global _HTML_PCRE_HREF_A
  contents = request_url_contents(*args, **kwargs)
  links    = _HTML_PCRE_HREF_A.findall(contents)
  hrefs    = [href for href,txt in links]
  return hrefs
  


#def request_list_dir(url, username='', password=''):
#  href_pattern = re.compile(r'(?<=\<a href\=\")(?P<dir>.*?)(?=\"\>(?P=dir)\<\/a\>)')
#  last_modified_pattern = re.compile('(?:'+')|(?:'.join(date_time_re_patterns)+')')
#  contents = request_url_contents(url,username,password,decode=True)
#  if(not contents):
#    return None
#  last_modified = last_modified_pattern.findall(contents)
#  for i in range(len(last_modified)):
#    dt = last_modified[i]
#    date_time_parse_string = ''
#    for j in range(len(date_time_re_patterns)):
#      if(re.compile(date_time_re_patterns[j]).match(dt)):
#        date_time_parse_string = date_time_parse_patterns[j]
#        last_modified[i] = datetime.datetime.strptime(dt,date_time_parse_string)
#  return ({'dirs': re.findall(href_pattern,contents),
#      'last_modified': last_modified
#      })
def request_list_dir(*args, **kwargs):
  #href_pattern = re.compile(r'(?<=\<a href=")(?P<dir>.*?)(?=">(?P=dir)</a>)')
  href_pattern = re.compile(r'(?<=\<a href=")(?P<href>.*)(?=">(?P<txt>.*)</a>)')
  #last_modified_pattern = re.compile('(?:'+')|(?:'.join(date_time_re_patterns)+')')
  contents = request_url_contents(*args, **kwargs)
  if (not contents):
    return None
  last_modified = last_modified_pattern.findall(contents)
  for i in range(len(last_modified)):
    dt = last_modified[i]
    date_time_parse_string = ''
    for j in range(len(date_time_re_patterns)):
      if(re.compile(date_time_re_patterns[j]).match(dt)):
        date_time_parse_string = date_time_parse_patterns[j]
        last_modified[i] = datetime.datetime.strptime(dt,date_time_parse_string)
  return ({'dirs': re.findall(href_pattern,contents),
      'last_modified': last_modified
      })

def createURL(*urls):
  urls=list(urls)
  for i in range(len(urls)):
      urls[i]=urls[i].strip('\\/')
  return '/'.join(urls)
  
