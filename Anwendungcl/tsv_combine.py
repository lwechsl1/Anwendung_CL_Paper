import pandas as pd

files = ['Dataset/TREC-perturbed-char-deletion.tsv', 'Dataset/TREC-perturbed-char-insertion.tsv', 'Dataset/TREC-perturbed-char-letter-case-changing.tsv', 'Dataset/TREC-perturbed-word-deletion.tsv', 'Dataset/TREC-perturbed-word-ordering.tsv', 'Dataset/TREC-perturbed-word-repetition.tsv']

combined_df = pd.concat([pd.read_csv(f, sep='\t', encoding='ISO-8859-1') for f in files])

combined_df.to_csv('combined.tsv', sep='\t', index=False)