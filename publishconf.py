# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# NB : l'Action GitHub (getpelican github_pages.yml) écrase SITEURL avec
# l'URL GitHub Pages réelle (https://sevres-karate.fr) au moment du build.
SITEURL = "https://sevres-karate.fr"
PATH = "content"
RELATIVE_URLS = False

# Sitemap (plugin pelican-sitemap) : mettre en avant les vraies pages de
# contenu (articles, pages) et déprioriser les index (catégories, tags...).
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.8,
        "pages": 0.7,
        "indexes": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "pages": "monthly",
        "indexes": "weekly",
    },
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
