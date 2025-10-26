#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

##################
#import urllib, hashlib

## Conf for pulling Gravatar Image
#EMAIL = u'vensder@gmail.com'
#DEFAULT_GRV_URL = u'images/tuxup_100.jpg'
#GRV_SIZE = 120

## construct gravatar URL
#GRV_URL = "http://www.gravatar.com/avatar/" + hashlib.md5(EMAIL.lower()).hexdigest() + "?"
#GRV_URL += urllib.urlencode({'d':DEFAULT_GRV_URL, 's':str(GRV_SIZE)})
###################

AUTHOR = u'Vensder'
SITENAME = u'Vensder\'s B10g'
SITEURL = 'https://vensder.github.io'

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

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
SOCIAL = (
          ('external-link-square', 'http://linuxforchildren.com'),
          ('linkedin-square', 'https://www.linkedin.com/in/vensder'),
          ('facebook-square', 'https://www.facebook.com/vensder'),
          ('twitter-square', 'https://twitter.com/v3n5d3r')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# themes: /usr/local/lib/python2.7/site-packages/pelican/themes
# Flex  lannisport  notmyidea  pelican-bootstrap3  simple

#THEME = "themes/pelican-sundown"
THEME = "themes/pure-single"

SITELOGO = "images/tuxup_100.jpg"

DISQUS_SITENAME = "vensdersb00l10g"

COVER_IMG_URL = "https://vensder.github.io/images/datacenter.jpg"

PROFILE_IMG_URL = "https://vensder.github.io/images/tuxup.jpg"

FAVICON_URL = "https://vensder.github.io/favicon.ico"
