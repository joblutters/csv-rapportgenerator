# csv-rapportgenerator

Zet een CSV met leaseaanvragen om in een overzichtsrapport.

## Het probleem
Een teamleider wil regelmatig weten hoeveel leaseaanvragen goedgekeurd, nog in behandeling of afgewezen zijn. De aanvragen komen als CSV-export uit het systeem. Nu wordt dat handmatig gefilterd en geteld in Excel. Dat kost tijd en er gaat snel iets mis.

## Wat het script doet
- Leest de aanvragen in uit een CSV-bestand
- Telt het totaal aantal aanvragen
- Geeft het aantal per status weer
- Berekent het totale leasebedrag per status
- Schrijft het rapport weg naar `rapport.txt`
- Geeft een duidelijke melding als het CSV-bestand ontbreekt

De voorbeelddata in `data/aanvragen.csv` is fictief.

## Voorbeeld-output
```
Aantal aanvragen: 18

Aantal per status:
  goedgekeurd: 9
  in behandeling: 5
  afgewezen: 4

Totaal leasebedrag per status:
  goedgekeurd: € 348300
  in behandeling: € 167100
  afgewezen: € 137300
```

## Gebruik
Windows:
```
py rapport.py
```
macOS/Linux:
```
python3 rapport.py
```
Het rapport verschijnt op het scherm en in `rapport.txt`.

## Gemaakt met
- Python 3 (pathlib)

## Status
Af.

Mogelijke uitbreiding: de `csv`-module gebruiken in plaats van `split(',')`, zodat ook velden met een komma erin goed worden ingelezen.