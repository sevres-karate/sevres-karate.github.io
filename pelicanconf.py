AUTHOR = 'Sèvres Karaté 92'
SITENAME = 'Sèvres Karaté 92'
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
DEFAULT_DATE_FORMAT = "%d/%m/%Y"

ARTICLE_ORDER_BY = "date"
DEFAULT_DATE_ORDER = "reversed"

# Blogroll
LINKS = (
    ("Inscription en ligne", "https://www.helloasso.com/associations/co-sevres-karate/adhesions/inscription-saison-2026-2027"),
    ("Fiche d'inscription 2026-2027", "https://sevres-karate.fr/pdfs/fiche_inscription_coskarate_2026-2027.pdf"),
    
    ("Fédération Française de Karaté", "https://www.ffkarate.fr/karate/"),
    ("Ligue des Hauts-de-Seine de Karaté", "https://sites.ffkarate.fr/hautsdeseine/"),
    ("Japan Karate Association", "http://www.jka.or.jp/"),
    ("Les Érables", "http://leserables-salons.com/")

)

# Social widget
SOCIAL = (
    ("Facebook", "https://www.facebook.com/p/CO-S%C3%A8vres-Karat%C3%A9-100066929041271/"),
    # ("Instagram", "#"),
)

DEFAULT_PAGINATION = 10

# La racine du site est la page « Accueil » (content/pages/accueil.html, qui
# porte save_as: index.html) : c'est elle que doivent servir les moteurs de
# recherche. Le gabarit index.html du thème n'est donc plus généré — il
# doublonnait la catégorie « Actu », toujours accessible par le menu.
INDEX_SAVE_AS = ""

PAGINATED_TEMPLATES = {
    "tag": None,
    "category": None,
    "author": None,
}

THEME = 'theme/karate'

STATIC_PATHS = [
    "images",
    "pdfs",
    "extra/robots.txt",
    "extra/favicon.ico",
    "extra/membres.enc.json",
    "extra/accueil_redirect.html",
]

# content/extra/ ne contient que des fichiers recopiés tels quels ; sans cette
# exclusion, Pelican essaie de lire accueil_redirect.html comme un article.
ARTICLE_EXCLUDES = ["pages", "extra"]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/membres.enc.json': {'path': 'membres.enc.json'},
    # L'accueil est passé de /pages/accueil.html à la racine : on garde une
    # redirection à l'ancienne adresse (favoris, liens déjà indexés).
    'extra/accueil_redirect.html': {'path': 'pages/accueil.html'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
