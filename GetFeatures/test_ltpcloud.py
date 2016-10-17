# -*- coding:utf8 -*-
import urllib


if __name__ == '__main__':
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = { 
        'api_key' : 'L8V2b6E3LaRjAJcTeySwDZKMjM8q2LFkBFslrCvi',
        'text' : '我是中国人。',
        'pattern' : 'ws',
        'format' : 'json'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
    content = result.read().strip()
    print content
