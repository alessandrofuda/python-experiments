import csv

new_csv_data = []
for n in range(1, 6):
    filename = f'data/split/huge-{n}.csv'
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_csv_data.append([
                row['aaaaaa'],
                row['bbbbbbbb'],
                row['cccccccc'],
                row['dddddddd'],
            ])


with open('data/full/huge-full.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'new_aaaaaa',
        'new_bbbbbb',
        'new_cccccc',
        'new_dddddd',
    ])
    writer.writerows(new_csv_data)
