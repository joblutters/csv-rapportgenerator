# csv-rapportgenerator

Zet een CSV met leaseaanvragen om in een overzichtsrapport.

## Het probleem
Een teamleider wil regelmatig weten hoeveel leaseaanvragen goedgekeurd, nog in behandeling of afgewezen zijn. De aanvragen komen als CSV-export uit het systeem. Nu wordt dat handmatig gefilterd en geteld in Excel. Dat kost tijd en er gaat snel iets mis.

## Wat het script doet
- Leest de aanvragen in uit een CSV-bestand
- Telt het totaal aantal aanvragen
- Geeft het aantal per status weer

De voorbeelddata in `data/aanvragen.csv` is fictief.

## Voorbeeld-output
```
Aantal aanvragen: 18
goedgekeurd: 9
in behandeling: 5
afgewezen: 4
```

## Gebruik
```
python rapport.py
```

## Gemaakt met
- Python 3 (pathlib)

## Status
In ontwikkeling. Gepland: totaal leasebedrag per status en het rapport wegschrijven naar een bestand.