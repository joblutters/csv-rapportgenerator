from pathlib import Path

path = Path('data/aanvragen.csv')
contents = path.read_text()

lines = contents.splitlines()

aanvragen = lines[1:]

print(f"Aantal aanvragen: {len(aanvragen)}")