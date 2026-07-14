#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chiffre le contenu réservé aux membres (tools/membres_content.html) et écrit
le blob chiffré dans content/extra/membres.enc.json.

Le déchiffrement se fait dans le navigateur (page « Accès Membres ») avec le
mot de passe du club. Rien n'est stocké en clair dans le site publié.

Utilisation :
    python tools/encrypt_membres.py "MOT_DE_PASSE_DU_CLUB"

Si aucun mot de passe n'est passé en argument, un mot de passe de DÉMO est
utilisé (voir MOT_DE_PASSE_DEMO ci-dessous) — à ne PAS utiliser en production.

Compatible Web Crypto : PBKDF2-HMAC-SHA256 + AES-256-GCM.
"""

import base64
import hashlib
import json
import os
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# --- Réglages -----------------------------------------------------------------
ITERATIONS = 200_000            # itérations PBKDF2 (doit matcher la page HTML)
MOT_DE_PASSE_DEMO = "sevres-karate-2026"   # mot de passe de DÉMO uniquement

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SOURCE = os.path.join(HERE, "membres_content.html")
DEST = os.path.join(ROOT, "content", "extra", "membres.enc.json")
# ------------------------------------------------------------------------------


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def main() -> None:
    password = sys.argv[1] if len(sys.argv) > 1 else MOT_DE_PASSE_DEMO
    if password == MOT_DE_PASSE_DEMO:
        print("!! Mot de passe de DÉMO utilisé (sevres-karate-2026).")
        print("   Pour la vraie mise en ligne : python tools/encrypt_membres.py \"votre-mot-de-passe\"")

    with open(SOURCE, "r", encoding="utf-8") as fh:
        plaintext = fh.read().encode("utf-8")

    salt = os.urandom(16)
    iv = os.urandom(12)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS, dklen=32)
    ciphertext = AESGCM(key).encrypt(iv, plaintext, None)  # renvoie ct || tag

    blob = {
        "salt": b64(salt),
        "iv": b64(iv),
        "ct": b64(ciphertext),
        "iterations": ITERATIONS,
        "v": 1,
    }

    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as fh:
        json.dump(blob, fh)

    print("OK -> {} ({} octets chiffrés)".format(DEST, len(ciphertext)))


if __name__ == "__main__":
    main()
