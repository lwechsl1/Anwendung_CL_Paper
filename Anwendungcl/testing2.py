import pandas as pd
from transformers import pipeline
import csv
import os
import torch

device = 0 if torch.cuda.is_available() else -1

#model_name="facebook/bart-large-mnli"
model_name="MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
classifier = pipeline("zero-shot-classification", model=model_name, device=device)
#when using noise data the label and text position are switched from the TREC DATA
# Load the data
#Dataset_name = "TREC"
#Dataset_name = "TREC-perturbed-char-deletion"
#Dataset_name = "TREC-perturbed-char-insertion"
#Dataset_name = "TREC-perturbed-char-letter-case-changing"
#Dataset_name = "TREC-perturbed-word-deletion"
#Dataset_name = "TREC-perturbed-word-ordering"
Dataset_name = "TREC-perturbed-word-repetition"


column_name_score = [model_name +"_"+ Dataset_name+"_score"]
column_name_label = [model_name +"_"+ Dataset_name+"_label"]

headers = [column_name_score,column_name_label]


filename_tsv = 'Dataset/' + Dataset_name +".tsv"

column2_data = []

with open(filename_tsv, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip the header
    for row in reader:
        column2_data.append(row[0])

candidate_labels = ["negative","positive"]

data_score = []
data_label = []
print(Dataset_name)

for i, review in enumerate(column2_data):
    result = classifier(review, candidate_labels)
    print(result)
    classification = result['labels'][0]
    confidence_score = result['scores'][0]
    #print(classification,confidence_score,review)
    data_score.append(confidence_score)
    data_label.append(classification)

global k
k=0
pathconstructor = model_name +"_" + Dataset_name + ".csv"
csv_gen_path = pathconstructor

directory = os.path.dirname(csv_gen_path)
if not os.path.exists(directory):
    os.makedirs(directory)

with open(csv_gen_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for value in data_score:
        writer.writerow([data_score[k], data_label[k]])
        k +=1

print("fertig")


