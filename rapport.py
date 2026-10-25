from pathlib import Path

path = Path('data/aanvragen.csv')
contents = path.read_text()

lines = contents.splitlines()

aanvragen = lines[1:]

print(f"Aantal aanvragen: {len(aanvragen)}")

aantal = {}

for aanvraag in aanvragen:
    kolommen = aanvraag.split(',')
    status = kolommen[-1].strip()

    if status in aantal:
        aantal[status] += 1        
    else:
        aantal[status] = 1    
        
print(aantal)