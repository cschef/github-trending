# coding: utf-8

import datetime
import codecs
import requests
import os
import time
from pyquery import PyQuery as pq


def scrape(language, filename):

    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }

    url = 'https://github.com/trending/{language}'.format(language = language)
    r = requests.get(url, headers = HEADERS)
    assert r.status_code == 200

    # print(r.encoding)

    d = pq(r.content)
    items = d('ol.repo-list li')

    # codecs to solve the problem utf-8 codec like chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## {language}\n'.format(language = language))

        for item in items:
            i = pq(item)
            title = i("h3 a").text()
            #owner = i("span.prefix").text()
            description = i("p.col-9").text()
            url = i("h3 a").attr("href")
            url = "https://github.com" + url
            # ownerImg = i("p.repo-list-meta a img").attr("src")
            # print(ownerImg)
            f.write(u"* [{title}]({url}):{description}\n".format(title = title, url = url, description = description))


def job():

    strdate = datetime.datetime.now().strftime('%Y-%m-%d')
    dirname = datetime.datetime.now().strftime('%Y/%m')
    filename = dirname + '/' + '{date}.md'.format(date = strdate)
    languageList = ['c', 'c++', 'c%23', 'java', 'python', 'html', 'css', 'javascript', 'shell', 'go']

    # create markdown file
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, 'w') as f:
        f.write('# GitHub Trending [' + strdate + ']\n')
        # write TOC
        f.write('\n## TOC\n\n')
        for lan in languageList:
            f.write('* [{lan}](#{lan})\n'.format(lan = lan))

    # write contents
    for lan in languageList:
        scrape(lan, filename)

