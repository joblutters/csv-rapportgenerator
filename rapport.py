from pathlib import Path

path = Path('data/aanvragen.csv')
contents = path.read_text()

lines = contents.splitlines()

aanvragen = lines[1:]

print(f"Aantal aanvragen: {len(aanvragen)}")

aantal = {}
    
totaal_bedrag = {}

for aanvraag in aanvragen:
    kolommen = aanvraag.split(',')
    status = kolommen[-1].strip()
    bedrag = int(kolommen[4]) 

    if status in aantal:
        aantal[status] += 1
        totaal_bedrag[status] += bedrag
    else:
        aantal[status] = 1
        totaal_bedrag[status] = bedrag
        
print("\nAantal per status:")
for status, stuks in aantal.items():
    print(f"  {status}: {stuks}")

print("\nTotaal leasebedrag per status:")
for status, bedrag in totaal_bedrag.items():
    print(f"  {status}: € {bedrag}")