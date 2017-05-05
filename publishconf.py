#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://icaroperseo.github.io'
RELATIVE_URLS = False

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = None
TAG_FEED_RSS = 'feeds/%s.rss.xml'

RSS_FEED_SUMMARY_ONLY = True

DELETE_OUTPUT_DIRECTORY = True

# Analytics settings
GOOGLE_ANALYTICS = 'UA-98215672-1'
GOOGLE_SITE_VERIFICATION = 'RhB2VdLzwEON-lx2UrogGDwcwqqASJ59IQpwU5w1iQ8'
PIWIK_URL = 'piwik-perseosblog.rhcloud.com'
PIWIK_SSL_URL = 'piwik-perseosblog.rhcloud.com'
PIWIK_SITE_ID = 1

# Comment settings
DISQUS_SITENAME = 'dual-temptation'
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True

# Addthis settings
ADDTHIS_PROFILE = 'ra-59098737798345e6'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

# deadlinks plugin settings
DEADLINK_VALIDATION = True

DEADLINK_OPTS = {
    'archive':  True,
    'labels':   True
}
