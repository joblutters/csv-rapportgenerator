from pathlib import Path

path = Path('data/aanvragen.csv')
contents = path.read_text()

lines = contents.splitlines()

aanvragen = lines[1:]

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

rapport = ""
rapport += f"Aantal aanvragen: {len(aanvragen)}\n"

rapport += "\nAantal per status:\n"
for status, stuks in aantal.items():
    rapport += f"  {status}: {stuks}\n"

rapport += "\nTotaal leasebedrag per status:\n"
for status, bedrag in totaal_bedrag.items():
    rapport += f"  {status}: € {bedrag}\n"

print(rapport)
path_rapport = Path('rapport.txt')
path_rapport.write_text(rapport, encoding='utf-8')