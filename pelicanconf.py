#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BlockDox'
SITENAME = 'BlockDox'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-bootstrap3'
# THEME = '/mnt/c/Users/dom_t/Desktop/Projects/pelican/blockdoxcom/themes/pelican-bootstrap3'
#DISPLAY_PAGES_ON_MENU = True
# Bootstrap theme settings
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'image_process']
# Set this to change bootswatch (http://bootswatch.com/)
#BOOTSTRAP_THEME = 'flatly'
CUSTOM_CSS = 'theme/css/custom.css'
CUSTOM_JS = 'theme/js/custom.js'
SITELOGO = 'images/logo-main.png'
HIDE_SITENAME = True
# Set this to true for the menu to be full width
#BOOTSTRAP_FLUID = False
#RELATIVE_URLS = True
#PAGE_URL = 'pages/{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
SHOW_ARTICLE_CATEGORY = True

# Defines the menu items in the top bar
MENUITEMS = (
    ('Home', SITEURL),
    ('About', SITEURL + '/pages/standard-text.html'),
    ('Smart Buildings', SITEURL + '/pages/smart-buildings.html'),
    ('Passenger Count', SITEURL + '/pages/passenger-count.html'),
    ('Articles', SITEURL + '/pages/articles.html'),
    ('Contact', SITEURL + '/pages/contact.html'),
)

# DIRECT_TEMPLATES = [
#   'index', 'categories', 'authors', 'archives',  # (default)
#  'contact'  # other HTML template to render
# ]

IMAGE_PROCESS = {
    'article-summary-image': ["scale_in 200 200 True"],
    'article-image': ["scale_in 500 500 True"],
    'page-image': ["scale_in 500 500 True"]
}
IMAGE_PROCESS_DIR = 'processed'
# For development always process
# IMAGE_PROCESS_FORCE = True

# Blogroll
LINKS = (
    ('BlockDox.com', 'http://blockdox.com'),
)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/company/blockdox/'),
          ('Twitter', 'https://twitter.com/blockdoxuk'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = [
    'admin/index.html',
    'admin/config.yml',
    'images',
    'extra'
]

PAGE_EXCLUDES = [
    'admin'
]

ARTICLE_EXCLUDES = [
    'admin'
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/Forza-Medium.otf': {'path': 'static/fonts/Forza-Medium.otf'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/LICENSE': {'path': 'LICENSE'},
    # 'extra/README': {'path': 'README'},
}

DISPLAY_ARTICLE_INFO_ON_INDEX = False

NETLIFY_CMS = True
TYPOGRIFY = False

# Import local development config
try:
    import pelicanconf_local
except ImportError:
    pass
