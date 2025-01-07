import csv

rows = []

with open('layoffs.csv', 'r') as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        rows.append(row)


with open('layoffs_quries.txt', 'w') as txt:
    base_string = 'INSERT INTO layoffs VALUES'
    for r in rows:
        txt.write(base_string + '(')
        i = 1
        for _ in r:
            if i < 9:
                if _ != 'NULL' and (i != 4 or i != 9):
                    txt.write(f'"{_}",')
                else:
                    txt.write(f'{_},')
            else:
                txt.write(_)
            i += 1
        txt.write(');\n')
            