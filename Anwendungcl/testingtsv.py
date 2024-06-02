import csv

# Define the path to your input and output CSV files
input_csv_file = 'data_train.csv'
output_csv_file = 'reduced_output.csv'

# Define the number of rows to save for each label
rows_per_label = 50

# Initialize counters for the number of rows saved for each label
label_0_count = 0
label_1_count = 0

# Open the input CSV file for reading and the output CSV file for writing
with open(input_csv_file, mode='r', newline='') as input_file, open(output_csv_file, mode='w',
                                                                    newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Iterate through the rows in the input CSV file
    for row in csv_reader:
        # Check if the row contains the label and text columns
        if len(row) >= 2:
            label = row[0]
            text = row[1]

            # Check if the label is '0' or '1' and if the respective count is less than the desired number of rows per label
            if label == '0' and label_0_count < rows_per_label:
                csv_writer.writerow(row)
                label_0_count += 1
            elif label == '1' and label_1_count < rows_per_label:
                csv_writer.writerow(row)
                label_1_count += 1

            # Check if the desired number of rows for both labels have been saved
            if label_0_count >= rows_per_label and label_1_count >= rows_per_label:
                break

print(f"Saved {label_0_count} rows with label '0' and {label_1_count} rows with label '1' to '{output_csv_file}'.")
