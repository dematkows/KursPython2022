# 1. Otwórz dowolny plik np. tekst.txt i wklej do niego fragment inwokacji Pana Tadeusza

filename = 'tekst.txt'

with open(filename, 'w', encoding="utf-8") as f:
    f.write("Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. "
            "Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie.")
