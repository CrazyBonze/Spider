#!/usr/bin/env python3
from urllib.parse import urlparse

#Get the domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' +results[-1]
    except:
        return ''

#Get the sub domain name
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
