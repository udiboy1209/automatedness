#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Meet Udeshi'
SITENAME = 'Meet Udeshi'
SITEURL = ''
THEME = 'themes/mine'
SLUGIFY_SOURCE = 'basename'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = False

ARTICLE_PATHS = ['blog', 'projects']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

DIRECT_TEMPLATES = ['blog']

STATIC_PATHS = ['images', 'pdfs']
