#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    # Nettoyage de la ligne
    line = line.strip().lower()
    # Suppression des caractères non alphabétiques
    words = re.findall(r"[a-zàâçéèêëîïôûùüÿñæœ]+", line)

    for word in words:
        print(f"{word}\t1")
