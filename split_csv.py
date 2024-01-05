import csv
chunk = []
row_count = 0
file_number = 1
header = ''

with open('data/huge.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if header == '':
            header = row
            continue

        # populate data/chunk
        chunk.append(row)
        row_count += 1
        if row_count >= 40:
            # write chunk to file
            with open(f'data/split/huge-{file_number}.csv', 'w') as new_file:
                writer = csv.writer(new_file)
                writer.writerow(header)
                writer.writerows(chunk)
            chunk = []
            file_number += 1
            row_count = 0

    if chunk:
        with open(f'data/split/huge-{file_number}.csv', 'w') as new_file:
            writer = csv.writer(new_file)
            writer.writerow(header)
            writer.writerows(chunk)
