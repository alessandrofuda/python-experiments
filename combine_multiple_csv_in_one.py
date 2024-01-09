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


            # ....... todo .................   ..wip.. see  https://www.youtube.com/watch?v=hE3O5hdE3Fs