#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: TrC
"""
import requests 
import re
from glob import glob
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
    return int(num)

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
def fd_list(fd):
    file_name = os.path.join(fd, '*.*')
    file_list = glob(file_name)
    print(file_list)
    file_list.sort(key=lambda f:int(re.sub('\D','',f)))
    print('v'*20)
    print(file_list)
    print('#'*20)
    return file_list

def writefile(fd, f_ls):
    imgtag = '<img src="{}" width="100%"/>\n'
    html_fname = os.path.join(fd, '00.html')
    with open(html_fname, 'w') as n_htm:
        n_htm.write('<html><head></head>\n')
        n_htm.write('<body bgcolor="#555555">\n')
        n_htm.write('<table width="1000" align="center">\n')
        n_htm.write('<tr><td width="100%">\n')
        n_htm.write('<h1 align="center">')
        n_htm.write(fd)
        n_htm.write('</h1>')
        n_htm.write('</td></tr>\n')
        for nm in file_list:
            fn = os.path.split(nm)[1]
            n_htm.write('<tr><td>\n')
            print(imgtag.format(fn))
            n_htm.write(imgtag.format(fn))
            n_htm.write('<br/>\n')
            n_htm.write('</td></tr>\n')
        n_htm.write('</table></body></html>\n')
    return

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
        file_list = fd_list(fd)
        writefile(fd, file_list)
    else:
        print('Download progress suck at {}'.format(num))
