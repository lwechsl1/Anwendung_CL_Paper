import pandas as pd
from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Load the data
file_path = 'imdb_converted_train01.csv'  # Adjust this to your actual file path
df = pd.read_csv(file_path)

# Get the first 5 reviews
reviews = df['text'].head(5).tolist()

# Define candidate labels
candidate_labels = ["positive", "negative"]

# Classify the first 5 reviews
for i, review in enumerate(reviews):
    result = classifier(review, candidate_labels)
    classification = result['labels'][0]  # Get the highest scoring label
    confidence_score = result['scores'][0]  # Get the score for the highest scoring label
    print(f"Review {i+1}: {review}\nClassification: {classification} (Confidence: {confidence_score:.4f})\n")
