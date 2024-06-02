import csv
import time
filename_tsv = 'Dataset/TREC.tsv'
filename_csv = 'MoritzLaurer/deberta-v3-large-zeroshot-v2.0_TREC-perturbed-word-repetition.csv'
tsv_gold = []
tsv_gold_txt = []
local_standard_score = []
local_standard_lable = []


with open(filename_tsv, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip the header
    for row in reader:
        tsv_gold.append(row[2])
        tsv_gold_txt.append(row[1])

with open(filename_csv, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        local_standard_score.append(row[0])
        local_standard_lable.append(row[1])


print(tsv_gold_txt[0])

negative = "negative"
positive = "positive"

count_bad=0
index_not_correct = []
correct_counter = 0
correct_conv_score = 0
for x in range(800):
    try:
        integer_value = int(tsv_gold[x])
    except ValueError:
        print(f"Error: '{string_value}' is not a valid integer.")
    print(x)
    if (local_standard_lable[x] == negative and integer_value == 0) or (
            local_standard_lable[x] == positive and integer_value == 1):
        print("local lable: ",local_standard_lable[x],"gold standart: ",tsv_gold[x])
        correct_counter+=1
        correct_conv_score += float(local_standard_score[x])
    else:

        print("local lable: ",tsv_gold[x],"gold standart: ",tsv_gold[x])
        print("bad at ", x,"bad classification nr." ,count_bad)
        count_bad+=1
        index_not_correct.append(x)

average_conv_score_correct = correct_conv_score /correct_counter
print("average confidence score for correct label: ", average_conv_score_correct)
print("correct found: ", correct_counter)
print("false found", count_bad)

print(average_conv_score_correct,", (",correct_counter,"/",count_bad,")")
