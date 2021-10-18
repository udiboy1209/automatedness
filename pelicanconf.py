#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PLUGINS = ['render_math']

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

STATIC_PATHS = ['images', 'pdfs']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
}

AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

MATH_JAX = {'color':'blue','align':'left'}
JINJA_ENVIRONMENT = {'extensions': ['jinja2_highlight.HighlightExtension']}
