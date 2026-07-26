PHOTOS DES MEMBRES DU BUREAU
(page « Le bureau » du site : content/c03_le-bureau.md)

Tant qu'une photo est absente, la vignette affiche les initiales du membre.
Les photos peuvent donc etre ajoutees une par une, sans rien casser.

--- COMMENT AJOUTER UNE PHOTO -------------------------------------------

1. Deposer l'image dans content/images/bureau/ (creer le dossier la
   premiere fois). Format CARRE, ~500x500 px, .jpg.

   Cadrage : la vignette est ronde, mais au survol de la souris la photo
   s'agrandit et redevient un carre arrondi (les coins masques par le
   cercle apparaissent alors). Cadrer donc en buste - tete + haut du
   torse - plutot qu'en gros plan sur le visage : le visage doit rester
   dans le cercle, et le reste devient visible a l'agrandissement.

2. Dans content/c03_le-bureau.md, sur la fiche du membre concerne,
   remplacer la ligne :

      <div class="bur-photo bur-photo-vide" aria-hidden="true">BM</div>

   par :

      <div class="bur-photo"><img src="/images/bureau/bruno-moustacchi.jpg" alt="Bruno Moustacchi" loading="lazy"></div>

3. Rebuilder le site pour verifier le rendu, puis commit + push.

--- NOMS DE FICHIERS SUGGERES -------------------------------------------

   bruno-moustacchi.jpg      (BM - President)
   nicolas-demirdjian.jpg    (ND - Secretaire)
   pierrick-bonneau.jpg      (PB - Tresorier)
   ludovic-chemin.jpg        (LC - Communication externe)
   franck-bricout.jpg        (FB - Evenements)
   philippe-vibien.jpg       (PV - Digital et images)

Rappel : ne publier une photo qu'avec l'accord de la personne concernee.
