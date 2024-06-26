import nltk
import csv
from random import seed
from random import randint

seed(1)


# --------------------------------------------------------------------------------------------------------------------

def return_random_number(begin, end):
    return randint(begin, end)


# --------------------------------------------------------------------------------------------------------------------

input_address = 'Dataset\\TREC.tsv'

output_text = 'text' + '\t' + 'label' + '\n'

with open(input_address) as input_file:
    input_data = csv.reader(input_file, delimiter='\t')

    line_num = 0

    for row in input_data:

        if (line_num > 0):

            print(row[0], '\t', row[1])

            is_sample_perturbed = False

            sample_text = row[1]
            sample_label = row[0]
            sample_tokenized = nltk.word_tokenize(sample_text)

            random_word_index = 0
            random_word_selected = False

            while (random_word_selected != True):
                random_word_index = return_random_number(0, len(sample_tokenized) - 1)
                if (len(sample_tokenized[random_word_index]) > 1):
                    random_word_selected = True

            print('Selected random word:', sample_tokenized[random_word_index])

            # --------------------------- reconstruct the perturbed sample

            perturbed_sample = ""

            for i in range(0, random_word_index):
                perturbed_sample += sample_tokenized[i] + ' '

            for i in range(random_word_index + 1, len(sample_tokenized)):
                perturbed_sample += sample_tokenized[i] + ' '

            is_sample_perturbed = True

            print('Perturbed sample:', perturbed_sample)

            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'

            print('----------------------------------------------------------')
        line_num += 1

output_file = open('Dataset\\TREC-perturbed-word-deletion.tsv', 'w')
output_file.write(output_text)
output_file.close()

if __name__ == '__main__':
    pass
