import csv

mitfcu = list(csv.DictReader(open("mitfcu.csv", 'rU')))

initialColumns = sorted(mitfcu[0].keys())


def parseTypeLookupLine(line):
    parts = line.strip().split()
    category = parts[0]
    pattern = " ".join(parts[1:])
    return (pattern, category)

memoLookup = [parseTypeLookupLine(l) for l in open("typeLookup.txt")]


def inferType(row):
    memo = row['Memo'].lower()
    for (pattern, category) in memoLookup:
        if pattern in memo:
            return category
    return None

for row in mitfcu:
    row['Type'] = inferType(row)

with open('mitfuInferredTypes.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames = initialColumns + ['Type'])

    writer.writeheader()
    for row in mitfcu:
        writer.writerow(row)

