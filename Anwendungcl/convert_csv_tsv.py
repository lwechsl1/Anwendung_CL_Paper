import csv
import os

csv_file_path = 'Dataset/data_test.csv'
tsv_file_path = 'Dataset/Imdb.tsv'

if not os.path.isfile(csv_file_path):
    print(f"Error: The file '{csv_file_path}' does not exist.")
else:
    # Open the CSV file for reading and the TSV file for writing
    with open(csv_file_path, mode='r', newline='') as csv_file, open(tsv_file_path, mode='w', newline='') as tsv_file:
        csv_reader = csv.reader(csv_file)
        tsv_writer = csv.writer(tsv_file, delimiter='\t')

        for row in csv_reader:
            # Clean the row if necessary (e.g., replace tabs if they exist in data)
            cleaned_row = [field.replace('\t', ' ') for field in row]
            tsv_writer.writerow(cleaned_row)

    print(f"CSV file '{csv_file_path}' has been successfully converted to TSV file '{tsv_file_path}'.")
