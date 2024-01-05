import csv


def write_chunk_to_file(filename, data_chunk, data_header=None):
    with open(filename, 'w') as new_file:
        writer = csv.writer(new_file)
        if data_header:
            writer.writerow(data_header)
        writer.writerows(data_chunk)


def fetch_split_path(original_filename):
    base_folder, name = original_filename.split('/')
    return base_folder + '/split/' + name


def split_csv(filename, chunk_rows_count=40):
    chunk = []
    current_row_number = 0
    file_number = 1
    header = ''
    original_filename, extension = filename.split('.')

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if header == '':
                header = row
                continue  # skip to next loop iteration

            # populate data/chunk
            chunk.append(row)
            current_row_number += 1
            if current_row_number >= chunk_rows_count:
                write_chunk_to_file(f'{fetch_split_path(original_filename)}-{file_number}.{extension}', chunk, header)
                chunk = []
                file_number += 1
                current_row_number = 0

        if chunk:
            write_chunk_to_file(f'{fetch_split_path(original_filename)}-{file_number}.{extension}', chunk, header)


split_csv('data/huge.csv')
