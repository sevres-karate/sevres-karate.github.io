=============================================================================
 PAGE « ACCÈS MEMBRES » — MODE D'EMPLOI
=============================================================================

À QUOI ÇA SERT
--------------
La page « Accès Membres » (menu « Le Club » > « Accès Membres ») affiche des
vidéos réservées aux membres, protégées par UN mot de passe unique du club.

Les vidéos ne sont PAS visibles dans le code du site : elles sont chiffrées
(AES-256-GCM). Seule une personne qui connaît le mot de passe peut les afficher,
le déchiffrement se faisant dans son navigateur.

Fichiers concernés :
  - tools/membres_content.html      -> le contenu EN CLAIR (à éditer)
  - tools/encrypt_membres.py        -> le script qui chiffre
  - content/extra/membres.enc.json  -> le résultat CHIFFRÉ (publié sur le site)
  - content/pages/acces-membres.html-> la page (formulaire + déchiffrement)


POUR CHANGER LES VIDÉOS
-----------------------
1) Ouvrir  tools/membres_content.html  et remplacer les identifiants de vidéos
   YouTube (voir les explications en haut du fichier).

2) Rechiffrer avec le VRAI mot de passe du club :

       python tools/encrypt_membres.py "le-mot-de-passe-du-club"

   (met à jour content/extra/membres.enc.json)

3) Régénérer le site :

       python -m pelican content -s pelicanconf.py

4) Prévisualiser en local :

       cd output
       python -m http.server 8000
   puis ouvrir  http://localhost:8000/pages/acces-membres.html


IMPORTANT — LE MOT DE PASSE
---------------------------
- Le mot de passe n'est écrit NULLE PART dans le site : il sert uniquement, au
  moment du chiffrement (étape 2), à verrouiller le contenu.
- Si on change le mot de passe, il faut rechiffrer (étape 2) et le recommuniquer
  aux membres.
- Le mot de passe de DÉMO actuel est « sevres-karate-2026 ». À REMPLACER par un
  vrai mot de passe avant la mise en ligne.

Ce mécanisme protège l'accès simple (il faut le mot de passe pour voir les
vidéos), mais ce n'est pas un coffre-fort militaire : un membre qui connaît le
mot de passe peut techniquement partager les vidéos. C'est le niveau de
protection normal et suffisant pour un club.
=============================================================================
