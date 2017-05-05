#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Icaro Perseo'
SITENAME = 'Dual Temptation'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),
 )

# Social widget
SOCIAL = (
          ('E-mail', '&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#100;&#117;&#97;&#108;&#116;&#101;&#109;&#112;&#116;&#97;&#116;&#105;&#111;&#110;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;', 'envelope'),
          ('GNU Social', 'https://quitter.se/icaroperseo', 'user'),
          ('Github', 'http://github.com/icaroperseo', 'github'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
                'images',
                'css/custom.css',
                'static/robots.txt'
]
EXTRA_PATH_METADATA = {
                       'css/custom.css': {'path': 'theme/css/custom.css'},
                       'static/robots.txt': {'path': 'robots.txt'}
}

# Theme
THEME = "themes/pelican-bootstrap3"
CUSTOM_CSS = 'theme/css/custom.css'
PYGMENTS_STYLE = 'zenburn'

SITELOGO = 'images/assets/dualtemptation.png'
SITELOGO_SIZE = 24
FAVICON = 'images/assets/favicon.ico'
AVATAR = 'images/assets/avatar.png'
ABOUT_ME = 'Eterno autodidacta, ex-colaborador de <em>Hackers & Developers</em> y cofundador de <em>&lt;°DesdeLinux</em>.'
CUSTOM_LICENSE='A menos que se indique lo contrario, todos los artículos se publican bajo la licencia <a href="https://www.gnu.org/licenses/#FDL">GNU FDL</a>.'
SHOW_ARTICLE_AUTHOR = False
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_CATEGORY = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True


# Pelican plugin
PLUGIN_PATHS = [
                "plugins",
                "pelican-plugins"
]

PLUGINS = [
           'bootstrap-rst',
           'i18n_subsites',
           'tipue_search',
           'related_posts',
           'series',
           'tag_cloud',
           'sitemap',
           'filetime_from_git',
           'deadlinks',
           'pelican_gist'
]

LOAD_CONTENT_CACHE = False

JINJA_ENVIRONMENT = {
                     'extensions': ['jinja2.ext.i18n'],
}

# sitemap plugin settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# tipue_search plugin settings
DIRECT_TEMPLATES = (
                    'index',
                    'categories',
                    'authors',
                    'archives',
                    'search'
)

# tag_cloud plugin settings
TAG_CLOUD_STEPS = 3

# deadlinks plugin settings
DEADLINK_VALIDATION = True

DEADLINK_OPTS = {
    'archive':  True,
    'labels':   True
}
