#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: TrC
"""
import requests 
import re
from tqdm import trange
import urllib.request
import os
import sys

"""
https://i.nhentai.net/galleries/<num>/<num>.jpg
https://t.nhentai.net/galleries/<num>/<num>t.jpg
"""

def num_from_link(link):
    fn = link.rsplit('/',1)[1]
    num = fn.split('t')[0]
    return num

def get_links(cm_id):
    
    src = 'https://nhentai.net/g/{}/'.format(cm_id)
    
    webpage = requests.get(src).text
    
    pat = r'https\:\/\/t\.nhentai\.net/galleries/\d+/\d+t\.jpg'
    
    links = list(set(re.findall(pat, webpage)))
    
    links.sort(key=lambda f:num_from_link(f))
    
    for i in range(len(links)):
        links[i] = links[i].replace('//t.nhen', '//i.nhen').replace('t.jpg', '.jpg')
    return links

def downloadlinks(links, location, skip):
    if not os.path.isdir(location):
        print('no such dir:', location)
        return False, -1
    
    for i in trange(len(links)):
        b = os.path.split(links[i])[1]
        if i < skip:
            print('skip:', b)
            continue
        tar = os.path.join(location, b)
        try:
            urllib.request.urlretrieve(links[i], tar)
        except Exception as e:
            print(e)
            return False, i
    return True, 9999

if __name__ == '__main__':
    cm_id = sys.argv[1]
    fd = 'n-{}'.format(cm_id)
    if not os.path.isdir(fd):
        os.mkdir(fd)
    else:
        opt = input('dir {} already exist, continue?[Y|N|int:skip]'.format(fd))
        if opt == "Y" or opt == "y":
            skip = 0
        elif opt == "N" or opt == "n":
            print('Goodbye')
            sys.exit()
        elif opt.isdigit():
            skip = int(opt)
        else:
            print('Wrong input <{}>, exit.'.format(opt))
            sys.exit()
    links = get_links(cm_id)
    ret, num = downloadlinks(links, fd, skip)
    if ret:
        print('Completely download {} for {}'.format(len(links),cm_id))
    else:
        print('Download progress suck at {}'.format(num))
