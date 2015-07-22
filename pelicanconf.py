#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'Olga Botvinnik'
SITENAME = u'Graduate Bioinformatics Council'
SITEURL = ''
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'

# Blogroll
LINKS =  (('Bioinformatics@UCSD', 'http://bioinformatics.ucsd.edu/'),
          ('UCSD', 'http://ucsd.edu/'),
          )

# Social widget
SOCIAL = (('github-square', 'http://github.com/gbic-ucsd'),
          ('twitter-square', 'http://twitter.com/gbicucsd'),
          ('facebook-square', 'http://facebook.com/gbicucsd'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "twenty-pelican-html5up"

COVER_IMG_URL = "https://raw.githubusercontent.com/olgabot/olgabot.github.io-source/master/content/images/ordered_driftwood.jpg"
PROFILE_IMG_URL = "http://raw.githubusercontent.com/olgabot/olgabot.github.io-source/master/content/images/olga_icon_square.jpg"
TAGLINE = "We are the voice of the graduate students in UCSD's B"
DISQUS_SITENAME = "gbic-ucsd"

TYPOGRIFY = True

GOOGLE_ANALYTICS = "UA-53680167-1"

MENUITEMS = [('About', 'pages/about.html'),
             ('Events', 'pages/events.html'),
             ('Leadership', 'pages/leadership.html'),
             ('Blog', 'pages/archive.html'),
             ('Initiatives', 'pages/initiatives.html'),
             ('Contact us', 'pages/contact.html'),
]

# IPython notebook blog posts
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins/ipynb']
# PLUGINS = ['ipynb']

IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output'))]

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}
