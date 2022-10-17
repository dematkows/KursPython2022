# 1. Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę
# krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój
# pies, rasy border collie wabi się Dyzio”.

pupil = ('pies', 'border collie', 'Dyzio')
(zwierze, rasa, imie) = pupil

print(f"Mój {zwierze} rasy {rasa} wabi się {imie}.")
