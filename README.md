# GitHub Trending(Python)


## Intro
Tracking the most popular Github repos, updated daily(Python version)

inspired by [github-trending(Go Version)](https://github.com/josephyzhou/github-trending)


## Run

You need install `git`

```bash
$ git config --global user.name "username"
$ git config --global user.email "mail@qq.com"
$ ssh-keygen -t rsa -b 4096 -C "mail@qq.com"
```

You need install `pyquery` & `requests`

```bash
$ git clone https://github.com/rocj/github-trending.git
$ cd github-trending
$ pip install -r requirements.txt
$ nohup python -u main.py > out.log 2>&1 &
```
> Note: 解决 `lxml` 安装不上的方法
```bash
# ubuntu 14.04
sudo apt-get build-dep python3-lxml
sudo apt-get install libxml2-dev libxslt-dev python-dev
```
详情请看 [stackoverflow](http://stackoverflow.com/questions/5178416/pip-install-lxml-error)

## Advance

A better place to use the script is in VPS

* You should have a VPS first, and then you should Add SSH Keys of your VPS to Github

* Then you can run the code in VPS

Thus the code will run never stop

## Lisence

MIT