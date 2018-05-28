# coding: utf-8

import scraper

import os
import time
import datetime


def git_add_commit_push(date, filename):

    cmd_git_add = 'git add {filename}'.format(filename = filename)
    cmd_git_commit = 'git commit -m "{date}"'.format(date = date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)


# scrape & push to github repo
scraper.job()
strdate = datetime.datetime.now().strftime('%Y-%m-%d')
dirname = datetime.datetime.now().strftime('%Y/%m')
filename = dirname + '/' + '{date}.md'.format(date = strdate)
git_add_commit_push(strdate, filename)
