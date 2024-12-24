from wwlln.scripts.custom_logging import wwlln_logger
# Test various request types:
#r_dir = ureq.request_url_contents(url_navy_dir)
#r_txt = ureq.request_url_contents(url_navy_txt)
#r_img = ureq.request_url_contents(url_navy_img)
#r_404 = ureq.request_url_contents(url_navy_404)
#  wwlln_logger.debug('  apparent_encoding:    {}'.format(r.apparent_encoding))
#  wwlln_logger.debug('  encoding:         {}'.format(r.encoding))
#  wwlln_logger.debug('  headers:        {}'.format(r.headers))
#  wwlln_logger.debug('  is_permanent_redirect:  {}'.format(r.is_permanent_redirect))
#  wwlln_logger.debug('  is_redirect:      {}'.format(r.is_redirect))
#  wwlln_logger.debug('  json:           {}'.format(r.json))
#  wwlln_logger.debug('  links:          {}'.format(r.links))
#  wwlln_logger.debug('  ok:           {}'.format(r.ok))
#  wwlln_logger.debug('  raise_for_status:     {}'.format(r.raise_for_status))
#  wwlln_logger.debug('  raw:          {}'.format(r.raw))
#  wwlln_logger.debug('  reason:         {}'.format(r.reason))
#  wwlln_logger.debug('  request:        {}'.format(r.request))
#  wwlln_logger.debug('  status_code:      {}'.format(r.status_code))

import requests
#import urllib.request
import re
import datetime

_URL_REQUEST_TIMEOUT_S = 20
date_time_re_patterns = ['\\d{2}-.{3}-\\d{4} \\d{2}:\\d{2}',
          '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}']

date_time_parse_patterns = ['%d-%b-%Y %H:%M', '%Y-%m-%d %H:%M']
_HTML_PCRE_HREF_A = re.compile(r'(?<=\<a href=")(?P<href>.*?)(?=">(?P<txt>.*)</a>)')


def request_url(url, username='', password = '', timeout=10, allow_redirects=True):
  wwlln_logger.info(str(locals()))
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
  wwlln_logger.debug(f'requests.get(url={url}, auth=(username={username}, password={password}), timeout={timeout}, allow_redirects={allow_redirects})')
  return requests.get(url, auth=(username, password), 
                      timeout=timeout, allow_redirects=allow_redirects)


def request_url_contents(*args, decode=True, **kwargs):
  wwlln_logger.info(str(locals()))
  req     = request_url(*args, **kwargs)
  content = req.content
  if (decode and req.apparent_encoding):
    content = content.decode(req.apparent_encoding)
  return content


def request_url_links(*args, **kwargs):
  wwlln_logger.info(str(locals()))
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
  wwlln_logger.info(str(locals()))
  #href_pattern = re.compile(r'(?<=\<a href=")(?P<dir>.*?)(?=">(?P=dir)</a>)')
  href_pattern = re.compile(r'(?<=\<a href=")(?P<href>.*)(?=">(?P<txt>.*)</a>)')
  #last_modified_pattern = re.compile('(?:'+')|(?:'.join(date_time_re_patterns)+')')
  contents = request_url_contents(*args, **kwargs)
  if (not contents):
    wwlln_logger.warning('Found no directory contents!')
    return None
  #return href_pattern.findall(contents)
  #return ({'dirs': [href_match['txt'] for href_match in href_pattern.findall(contents)], 
  #return ({'dirs': [href_match[1] for href_match in href_pattern.findall(contents)], 
  #         'last_modified': datetime.datetime.now()})
  dirs          = [href_match[1] for href_match in href_pattern.findall(contents)]
  last_modified = (len(dirs) * [datetime.datetime.now()])
  wwlln_logger.warning('TODO: FIX - BLINDLY ADDING NOW() AS "LAST_MODIFIED"!!!')
  return {'dirs': dirs, 'last_modified': last_modified}
  #last_modified = last_modified_pattern.findall(contents)
  #for i in range(len(last_modified)):
  #  dt = last_modified[i]
  #  date_time_parse_string = ''
  #  for j in range(len(date_time_re_patterns)):
  #    if(re.compile(date_time_re_patterns[j]).match(dt)):
  #      date_time_parse_string = date_time_parse_patterns[j]
  #      last_modified[i] = datetime.datetime.strptime(dt,date_time_parse_string)
  #return ({'dirs': re.findall(href_pattern,contents),
  #    'last_modified': last_modified
  #    })

def createURL(*urls):
  wwlln_logger.info(str(locals()))
  urls=list(urls)
  for i in range(len(urls)):
      urls[i]=urls[i].strip('\\/')
  return '/'.join(urls)
  
