from email import charset, header
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re

def download(url):
    print('Downloading', url)
    try:
        response = urllib.request.urlopen(url)
        header = response.headers
        charset = header.get_content_charset(failobj='utf-8')
        html = response.read().decode(charset)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error', e.reason)
        html = None
    return header, html

header, html = download('''http://127.0.0.1:8000/places/default/sitemap.xml''')

print(html)

#print(html)

file_url = 'http://127.0.0.1:8000/places/default/sitemap.xml'
