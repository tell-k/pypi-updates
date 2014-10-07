==========================================
PyPI Recent Updates Bot
==========================================

Description
-----------------------------------------

* Twitter bot for PyPI Recent Updates
* https://twitter.com/pypi_updates

Required
-----------------------------------------

* `Heroku account <https://id.heroku.com/signup>`_
* `Heroku Toolbelt <https://devcenter.heroku.com/articles/getting-started-with-python#set-up>`_
* `Twitter account <https://twitter.com/signup>`_
* `Twitter API Tokens <https://apps.twitter.com/>`_

::

 Caution: Access level of your twitter apps must be "Read and write".


Setup
-----------------------------------------

1. Clone repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ git@github.com:tell-k/pypi-updates-bot.git


2. Create ".env" file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ cd pypi-updates-bot
 $ toucn .env

Write your Twitter API tokens

::

 # .env file
 TWITTER_CONSUMER_KEY=[your consumer key]
 TWITTER_CONSUMER_SECRET=[your consumer secret]
 TWITTER_ACCESS_KEY=[your access key]
 TWITTER_ACCESS_SECRET=[your access secret]

2. Create heroku apps and settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ heroku login
 $ heroku create
 $ heroku addons:add memcachier
 $ heroku plugins:install git://github.com/ddollar/heroku-config.git
 $ heroku config:push

Confirm enviroment values.

::

 $ heroku config
 === xxxxxx-xxxxxx-xxxx Config Vars
 MEMCACHIER_PASSWORD:     xxxxxxxxxx
 MEMCACHIER_SERVERS:      xxx.xxx.xxx.xxxxxxx.xxxx:xxxxxx
 MEMCACHIER_USERNAME:     xxxxxxxx
 TWITTER_ACCESS_KEY:      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 TWITTER_ACCESS_SECRET:   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 TWITTER_CONSUMER_KEY:    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 TWITTER_CONSUMER_SECRET: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

3. Deploy heroku apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ git push heroku master

 # Run the first time only
 $ heroku ps:scale bot=1

 # Confirm application log
 $ heroku logs -tail


LICENSE
-----------------------------------------

* MIT License
* See the LICENSE file for specific terms.

TODO
-----------------------------------------

* I'll use the shortened URL.
