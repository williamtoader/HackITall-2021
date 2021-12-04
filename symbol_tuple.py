
import csv
symbol_tuple = []
with open('Fortune500.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[2] != '':
                # print(f'{line_count} {row[2]}')
                symbol_tuple.append(row[2])
                line_count += 1
    # print(f'Processed {line_count} lines.')
    symbol_tuple = tuple(symbol_tuple)
