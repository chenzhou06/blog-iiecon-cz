#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chen Zhou'
SITENAME = 'Chen Zhou'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Miscellany'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Costumized
THEME = "cloud"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
