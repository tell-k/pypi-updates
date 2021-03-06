==========================================
pypi-updates
==========================================

|travis| |coveralls| |requires|

Description
-----------------------------------------

* Bot for PyPI Recent Updates
* Bot will check the latest RSS(https://pypi.python.org/pypi?:action=rss) once per minute.
* https://twitter.com/pypi_updates ... This account has been permanently frozen by Twitter.
* https://twitter.com/pypi_updates2

Required
-----------------------------------------

* `Heroku account <https://id.heroku.com/signup>`_
* `Heroku Toolbelt <https://devcenter.heroku.com/articles/getting-started-with-python#set-up>`_
* `Twitter account <https://twitter.com/signup>`_
* `Twitter API tokens <https://apps.twitter.com/>`_

::

 Caution: Access level of your twitter apps must be "Read and write".


Setup
-----------------------------------------

1. Clone repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ git clone git@github.com:tell-k/pypi-updates.git


2. Create ".env" file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ cd pypi-updates-bot
 $ toucn .env

Write your API tokens

::

 # .env file
 TWITTER_CONSUMER_KEY=[your consumer key]
 TWITTER_CONSUMER_SECRET=[your consumer secret]
 TWITTER_ACCESS_KEY=[your access key]
 TWITTER_ACCESS_SECRET=[your access secret]

3. Create heroku apps and settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ heroku login
 $ heroku apps:create pypi-updates
 $ heroku addons:add memcachier
 $ heroku plugins:install heroku-config
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

4. Deploy heroku apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

 $ git push heroku master

 # Run the first time only
 $ heroku ps:scale bot=1

 # Confirm application log
 $ heroku logs --tail

Licence
-----------------------------------------

* MIT License
* See the LICENSE file for specific terms.


.. |travis| image:: https://travis-ci.org/tell-k/pypi-updates.svg?branch=master
    :target: https://travis-ci.org/tell-k/pypi-updates
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/tell-k/pypi-updates/badge.png
    :target: https://coveralls.io/r/tell-k/pypi-updates
    :alt: coveralls.io

.. |requires| image:: https://requires.io/github/tell-k/pypi-updates/requirements.svg?branch=master
     :target: https://requires.io/github/tell-k/pypi-updates/requirements/?branch=master
     :alt: requires.io
