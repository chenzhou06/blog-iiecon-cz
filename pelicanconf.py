#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chen Zhou'
SITENAME = 'IIECON'
# SITESUBTITLE = "ChenZhou's blog"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = 'en'

# Costumized
DISPLAY_CATEGORIES_ON_MENU = True
LOCALE = ("usa")
THEME = "pelican-themes\\cebong_cos"

# Pulgins
PLUGIN_PATHS = ["pandoc_reader"]
PLUGINS = ["pandoc_reader"]

PANDOC_ARGS = [
        "--mathjax",
        "--smart",
        ]
PANDOC_EXTENSIONS = [
        "+definition_lists",
        ]

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
