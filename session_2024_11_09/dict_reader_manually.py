from pprint import pprint


def split(text):
    # Find the location of the comma separators
    splitting_points = []
    quote_started = False
    for i, c in enumerate(text):
        if c == '"':
            quote_started = not quote_started
        elif c == ',' and not quote_started:
            splitting_points.append(i)

    # Slice based on the location of the separators
    parts = []
    last_split = 0
    for i in splitting_points:
        parts.append(text[last_split:i])
        last_split = i + 1
    parts.append(text[last_split:])

    # Remove quotation marks
    for i in range(len(parts)):
        if parts[i].startswith('"') and parts[i].endswith('"'):
            parts[i] = parts[i][1:-1]
    return parts


with open('coffee.csv', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]
    headers = split(lines[0])

    records = []
    for line in lines[1:]:
        split_line = split(line)
        records.append({
            headers[i]: split_line[i] for i in range(len(headers))
        })

pprint(records[0])
