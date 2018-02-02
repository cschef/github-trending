# GitHub Trending

爬取 `GitHub Trending` 页面每天最活跃的项目，并自动提交到你的仓库

Scrape the most excited repos in Github Trending everyday, and automaticly commit to your GitHub repo.

> Transplant from [github-trending(Go Version)](https://github.com/josephyzhou/github-trending)

## Require

* git
* python 3.x
* pyquery & requests

## Usage

* Install `git` & config it

```bash
# install git (linux)
$ yum install git

# config your git
$ git config --global user.name "username"
$ git config --global user.email "mail@qq.com"
$ ssh-keygen -t rsa -b 4096 -C "mail@qq.com"
```

* Install python

* Fork this repo

* Clone your repo and Install `pyquery` & `requests`

```bash
$ git clone https://github.com/yourusername/github-trending.git
$ cd github-trending
$ pip install -r requirements.txt
```

* Run

```bash
nohup python -u scrape.py > out.log 2>&1 &
```

> Note: 解决 `lxml` 安装不上的方法
```bash
# ubuntu 14.04
sudo apt-get build-dep python3-lxml
sudo apt-get install libxml2-dev libxslt-dev python-dev
```
See it on [stackoverflow](http://stackoverflow.com/questions/5178416/pip-install-lxml-error)

## Lisence

MIT