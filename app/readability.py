import re

import requests

from config import parse_config

config = parse_config("local")

base_url = "https://www.readability.com/api/content/v1/parser"


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def parse_url(url):
    url = base_url + "?url=" + url
    params = {}
    params['token'] = config['readability_token']

    try:
        response = requests.get(url, params).json()
        print(url)
        if(response):
            if ('error' in response):
                return ''
            else:
                return response['title'].strip() + ' ' + striphtml(response['content']).strip()
        else:
            return ''
    except ValueError as e:
        return ''
