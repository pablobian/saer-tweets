saer-tweets
===========

Tweets Juan José Saer's quotes on https://twitter.com/jjsaer.

Juan José Saer on Wikipedia: [es](http://es.wikipedia.org/wiki/Juan_Jos%C3%A9_Saer), [en](http://en.wikipedia.org/wiki/Juan_Jos%C3%A9_Saer).

## Installation

```
pip install -r requirements.txt
```

Edit `config.py` with your account's creadentials and run

```
python jjsaer.py
```

to send your first tweet.

You may want to add this command to a cron job.

## Tweet other stuff or adding more quotes

Simply edit `saertweets.txt` separating tweets with one empty line and make sure each tweet is no longer thatn 140 chars.

## Crontab on a virtualenv instalation

This rule runs the script four times a day.

```crontab
0 0,4,8,12,16,20 * * * cd /path/to/saer-tweets; source venv/bin/activate; python jjsaer.py ; deactivate
```
