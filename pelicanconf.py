#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Katie Lefevre'
SITENAME = u'Katie Lefevre'
SITEURL = 'http://KatieLefevre.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME = './pelican_themes/html5-dopetrope'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
		('Interactive Python', 'http://runestoneinteractive.org/library.html'),
        ('This to That', 'http://www.thistothat.com/'),
        ('Rookie Mag', 'http://www.rookiemag.com/'),
        )

# Social widget
SOCIAL = (
			('Github', 'https://github.com/ktel1218/'),
			('Twitter', 'https://twitter.com/ktel1218'),
          )

TWITTER_USER = 'ktel1218'
GITHUB_USER = 'ktel1218'

ABOUT_TEXT = 'My name is Katie and I help budding programmers learn Python. Ask me about bugs.'
ABOUT_IMAGE = 'images/profile_img.jpeg'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
