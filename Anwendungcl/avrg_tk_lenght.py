import csv


def calculate_average_tokens_per_row_first_column(filename_tsv):
    total_tokens = 0
    total_rows = 0

    with open(filename_tsv, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')

        for row in reader:
            if row:
                first_column = row[1]
                tokens = first_column.split()
                total_tokens += len(tokens)
                total_rows += 1

    if total_rows == 0:
        return 0

    average_tokens_per_row = total_tokens / total_rows
    return average_tokens_per_row


# Example usage:
filename_tsv = 'Dataset/imdb.tsv'
average_tokens_per_row = calculate_average_tokens_per_row_first_column(filename_tsv)
print(f"Average number of tokens per row in the first column: {average_tokens_per_row:.2f}")
