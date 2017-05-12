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
$ python main.py
```

## Advance

A better place to use the script is in VPS

* You should have a VPS first, and then you should Add SSH Keys of your VPS to Github

* Then you can run the code in VPS

Thus the code will run never stop

## Special Day

- [2017-03-29](https://github.com/bonfy/github-trending/blob/master/2017-03-29.md) - my repo [qiandao](https://github.com/bonfy/qiandao) record by github-trending(python)

## Lisence

MIT
