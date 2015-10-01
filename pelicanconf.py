#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import urllib, hashlib

# Conf for pulling Gravatar Image
EMAIL = u'vensder@gmail.com'
DEFAULT_GRV_URL = u'images/tuxup_100.jpg'
GRV_SIZE = 120

# construct gravatar URL
GRV_URL = "http://www.gravatar.com/avatar/" + hashlib.md5(EMAIL.lower()).hexdigest() + "?"
GRV_URL += urllib.urlencode({'d':DEFAULT_GRV_URL, 's':str(GRV_SIZE)})

AUTHOR = u'Vensder'
SITENAME = u'Vensder\'s B00L10g'
SITEURL = 'http://vensder.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIN', 'https://www.linkedin.com/in/vensder'),
          ('FaceB00k', 'https://www.facebook.com/vensder'),
          ('7wi773r', 'https://twitter.com/v3n5d3r'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# themes: /usr/local/lib/python2.7/site-packages/pelican/themes
# Flex  lannisport  notmyidea  pelican-bootstrap3  simple

THEME = "themes/pelican-sundown"

#SITELOGO = "images/tuxup_100.jpg"

DISQUS_SITENAME = "vensdersb00l10g"
