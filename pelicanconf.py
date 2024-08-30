AUTHOR = 'Sèvres Karaté'
SITENAME = 'Sèvres Karaté'
SITESUBTITLE = 'Le karaté pour tous'

PATH = "content/"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SOCIAL_WIDGET_NAME = "Réseaux sociaux"
LINKS_WIDGET_NAME = "Liens"

# Blogroll
LINKS = (
    ("Fiche d'inscription 2024-2025", "{static}/pdfs/fiche_inscription_coskarate_2024-2025.pdf"),
    ("Federation Française de Karaté et Disciplines Associées", "http://www.ffkama.fr/"),
    ("Ligue des Hauts-de-Seine de Karaté", "http://www.ffkarate.fr/liguehautsdeseine/"),
    ("Japan Karate Association", "http://www.jka.or.jp/"),
    ("Club Olympique de Sèvres", "http://cosevres.fr/"),
    ("Les Érables", "http://leserables-salons.com/")

)

# Social widget
SOCIAL = (
    ("Instagram", "#"),
)

DEFAULT_PAGINATION = 10

THEME = 'theme/karate'

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
